#!/usr/bin/env python3.6
"""

TODO:

- docs/source links
  - how to find the source of a builtin module?
- header
  - src: https://github.com/westurner/python-file-funcs ?
  - note that this is run on a Posix machine
    - sys.platform ?
- footer

- add TODO's async library?
  - generalize the table generation code
    - this is the same as for the pathjoin code i wrote awhile back

- include propsed additions to pathlib
  - P for proposed?
"""

import collections
import functools
import inspect
import os as _os
import os.path as _ospath
import shutil as _shutil
import pathlib as _pathlib
import textwrap

import path as _path

meta = {}
meta['os'] = {
    'source': 'https://github.com/python/cpython/tree/3.6/Lib/os.py',
    'docs': 'https://docs.python.org/3/library/os.html',
    'docsbaseurl': 'https://docs.python.org/3/library/os.html#os.',
}
meta['os.path'] = {
    'source': [
        'https://github.com/python/cpython/blob/3.6/Lib/posixpath.py',
        'https://github.com/python/cpython/tree/3.6/Lib/ntpath.py',
        'https://github.com/python/cpython/tree/3.6/Lib/macpath.py'],
    'docs': 'https://docs.python.org/3/library/os.path.html',
    'docsbaseurl': 'https://docs.python.org/3/library/os.path.html#os.path.',
}
meta['shutil'] = {
    'source': 'https://github.com/python/cpython/tree/3.6/Lib/shutil.py',
    'docs': 'https://docs.python.org/3/library/shutil.html',
    'docsbaseurl': 'https://docs.python.org/3/library/shutil.html#shutil.',
}
meta['pathlib'] = {
    'source': 'https://github.com/python/cpython/blob/3.6/Lib/pathlib.py',
    'docs': 'https://docs.python.org/3/library/pathlib.html',
    'docsbaseurl': 'https://docs.python.org/3/library/pathlib.html#pathlib.Path.', #pathlib.PurePath.
}
meta['pathpy'] = {
    'source': [
        'https://github.com/jaraco/path.py/blob/master/path.py',
        'https://github.com/jaraco/path.py',
    ],
    'docs': 'https://pathpy.readthedocs.io/en/latest/',
    'docsbaseurl': 'https://pathpy.readthedocs.io/en/latest/api.html#path.Path.',
}

def maybe_list(obj):
    if isinstance(obj, (tuple, list)):
        return obj
    return (obj,)


def print_header__modules():
    print('Modules')
    print('+++++++++')
    for key, data in meta.items():
        print('- %s' % key)
        print('')
        for url in maybe_list(data['source']):
            print('  - Source: %s' % url)
        for url in maybe_list(data['docs']):
            print('  - Docs: %s' % url)
        print('')


mappings = {}
mappings['pathpy'] = {
    # 'getcwd': {
    #     'pathpy': 'getcwdu',
    # },
    'getsize': {
        'pathpy': 'size'
    },
}
mappings['pathlib'] = {
    'atime': {
        'pathpy': 'getatime',
        'os.path': 'getatime',
    },
    'ctime': {
        'pathpy': 'getctime',
        'os.path': 'getctime',
    },
    'mtime': {
        'pathpy': 'getmtime',
        'os.path': 'getmtime',
    },
    'cwd': {
        'pathpy': 'getcwd',
        'os': 'getcwd',
    },
    'owner': {
        'pathpy': 'get_owner',
    },
    'is_absolute': {
        'pathlib': 'absolute',
        'pathpy': 'isabs',
        'os.path': 'isabs',
    },
    'is_file': {
        'pathpy': 'isfile',
        'os.path': 'isfile',
    },
    'is_dir': {
        'pathpy': 'isdir',
        'os.path': 'isdir',
    },
    'is_symlink': {
        'pathpy': 'islink',
        'os.path': 'islink',
    },
    'joinpath': {
        'os.path': 'join'
    },
    'iterdir': {
        'pathpy': 'listdir',
    },
    # TODO
}


def build_seealso(mappings=mappings):
    """
    Kwargs:
        mappings (dict): ``{'pathlib': {'is_abs': {'pathpy': 'isabs'}}}``
    Returns:
        dict[attrname] = {destattr: [modnames]}
    """
    seealso = {}
    for mapsetname, mappingset in mappings.items():
        for attrname, mappings in mappingset.items():
            for modname, destattr in mappings.items():
                seealso.setdefault(attrname, {}).setdefault(destattr, {}).setdefault(modname, True)
                seealso.setdefault(destattr, {}).setdefault(attrname, {}).setdefault(mapsetname, True)
    return seealso


_Thing = collections.namedtuple('Thing',
    ('name', 'signature', 'docstring', 'source', 'iscallable', 'attr', 'obj'))


class Thing(_Thing):
    pass


def get_signatures(obj, additional_attrs=None):
    attrs = sorted(x for x in dir(obj) if not x.startswith('_'))
    if additional_attrs:
        attrs = sorted(attrs + additional_attrs)
    for attrname in attrs:
        try:
            attr = getattr(obj, attrname)
        except AttributeError:
            continue
        if inspect.isbuiltin(attr):
            iscallable = True
            try:
                signature = inspect.signature(attr)
            except ValueError:
                signature = attr.__class__ #TODO
            docstring = inspect.getdoc(attr)
            # source = inspect.getsource(attr)
            source = None
        elif (inspect.isfunction(attr) or inspect.ismethod(attr)):
            iscallable = True
            signature = inspect.signature(attr)
            docstring = inspect.getdoc(attr)
            source = inspect.getsource(attr)
        elif isinstance(attr, functools.partial):
            iscallable = True
            signature = inspect.signature(attr)
            docstring = inspect.getdoc(attr)
            source = None  # inspect.getsource(attr)
        else:
            iscallable = False
            signature = ''
            docstring = inspect.getdoc(attr)  # TODO
            source = None
        yield attrname, Thing(
            name=attrname,
            signature=signature,
            docstring=docstring,
            source=source,
            iscallable=iscallable,
            attr=attr,
            obj=obj)


def build_methods():
    methods = {}

    pathlib_path = _pathlib.Path #('/')
    methods['pathlib'] = dict(get_signatures(pathlib_path))

    pathpy_path = _path.Path #('/')
    methods['pathpy'] = dict(get_signatures(pathpy_path,
                                            ['__div__', '__rdiv__']))
    methods['os'] = dict(get_signatures(_os))
    methods['os.path'] = dict(get_signatures(_ospath))
    methods['shutil'] = dict(get_signatures(_shutil))
    return methods


def build_sets(methods):
    sets = {}
    sets['union'] = (
        set(methods['pathlib'])
        .union(methods['pathpy'])
        #.union(methods['os'])
        .union(methods['os.path'])
        #.union(methods['shutil'])
    )
    sets['union'].difference_update((
        'sys',
        'supports_unicode_filenames',
        'genericpath',
        #'sameopenfile',
        #'samestat',
        #'extsep',
        #'pathsep',
    ))
    sets['union'] = sorted(sets['union'])

    sets['pathlib_and_pathpy'] = sorted(
        set(methods['pathlib']).intersection(methods['pathpy']))
    sets['pathlib_not_pathpy'] = sorted(
        set(methods['pathlib']).difference(methods['pathpy']))
    sets['pathpy_not_pathlib'] = sorted(
        set(methods['pathpy']).difference(methods['pathlib']))
    return sets


methods = build_methods()
sets = build_sets(methods=methods)


def print_report_header():
    print('')
    print('==================================')
    print('Python file methods and attributes')
    print('==================================')
    print('')
    print('- Objective: Identify and compare Python file '
          'functions/methods and attributes from '
          'os, os.path, shutil, pathlib, and path.py')
    print('- Source: https://github.com/westurner/pyfilemods')
    print('- Docs: https://westurner.github.io/pyfilemods/')
    print('')
    print('Contents')
    print('++++++++')
    print('.. contents::')
    print('')

    print_header__modules()


print_report_header()


def print_table(sets=sets, methods=methods):
    hdr = '================== == ======= ====== ======= ======='
    print(hdr)
    print('attr               os os.path shutil pathlib path.py ')
    print(hdr)
    for attr in sets['union']:
        print('%-18s %-2s %-7s %-6s %-8s %-7s' % (
            '`%s`_' % attr,
            'X' if attr in methods['os'] else ' ',
            'X' if attr in methods['os.path'] else ' ',
            'X' if attr in methods['shutil'] else ' ',
            'X' if attr in methods['pathlib'] else ' ',
            'X' if attr in methods['pathpy'] else ' ',
        ))
    print(hdr)
    print('')


print('Sets')
print('++++')
print('')
print('attr table')
print('==========')
print('')
print_table(sets=sets, methods=methods)


def print_thing(varname, sets=sets):
    print(varname)
    print('='*len(varname))
    _var = sets[varname]
    for x in _var:
        print('- `%s`_' % x)


setnames = ['pathlib_and_pathpy', 'pathlib_not_pathpy', 'pathpy_not_pathlib']
for x in setnames:
    print_thing(x, sets=sets)
    print('')


def indent(text, n, char=' '):
    if not text:
        return text
    return textwrap.indent(text, char*n)


print('')
print('attrs')
print('+++++')
print('')


def print_code(obj, attr):
    _attr = getattr(obj, attr)
    if obj and _attr:
        print('')
        print('.. code:: python')
        #print('   :class: highlight')
        print('')
        print(indent(_attr, 4))
        print('')


def fmtsignature(obj):
    if obj is None:
        return '``None``'
    if obj.iscallable:
        return '``%s``' % obj.signature if obj.signature else ' '
    else:
        return '*attribute*'


def print_attr_methods(sets=sets, methods=methods):
    seealso = build_seealso(mappings=mappings)
    for method in sets['union']:
        methodstr = '``{}``'.format(method)
        print(methodstr)
        print('=' * (len(methodstr)+1))
        things = ['os', 'os.path', 'shutil', 'pathlib', 'pathpy',]
        attrs = {}
        for thing in things:
            attrs[thing] = methods[thing].get(method)

        for name in things:
            obj = attrs[name]
            if obj and obj.signature:
                print('| **%s.%s**\ %s' % (name, method, fmtsignature(obj)))
        print('')

        _seealso = seealso.get(method, {})
        if _seealso:
            seealsostrs = []
            for key, libs in _seealso.items():
                for lib in libs:
                    seealsostrs.append(
                        '`%s <#%s>`_' % ('%s.%s' % (lib, key), key.replace('_', '-')))
            print('| seealso: %s' % ', '.join(seealsostrs))
            print(' ')

        for modname in things:
            metadata = meta[modname]
            obj = attrs[modname]
            if obj: #and obj.iscallable:
                print('| **%s.%s**%s:' % (modname, method,
                        ('\ %s' % fmtsignature(obj) if obj and obj.signature else '')))
                print('| `source <%s>`__ `docs <%s%s>`__' % (
                    maybe_list(metadata['source'])[0],  # TODO
                    metadata['docsbaseurl'],
                    method))
                if obj.source:
                    print_code(obj, 'source')
                else:
                    print_code(obj, 'docstring')
        print('')


print_attr_methods(sets=sets, methods=methods)


if __name__ == '__main__':
    import sys
    if '-i' in sys.argv:
        import ipdb
        ipdb.set_trace()
