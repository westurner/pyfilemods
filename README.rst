
==================================
Python file methods and attributes
==================================

- Objective: Identify and compare Python file methods and attributes
- Source: https://github.com/westurner/pyfilemods
- Docs: https://westurner.github.io/pyfilemods/

Contents
++++++++
.. contents::

Modules
+++++++++
- os

  - Source: https://github.com/python/cpython/tree/3.6/Lib/os.py
  - Docs: https://docs.python.org/3/library/os.html

- os.path

  - Source: https://github.com/python/cpython/blob/3.6/Lib/posixpath.py
  - Source: https://github.com/python/cpython/tree/3.6/Lib/ntpath.py
  - Source: https://github.com/python/cpython/tree/3.6/Lib/macpath.py
  - Docs: https://docs.python.org/3/library/os.path.html

- shutil

  - Source: https://github.com/python/cpython/tree/3.6/Lib/shutil.py
  - Docs: https://docs.python.org/3/library/shutil.html

- pathlib

  - Source: https://github.com/python/cpython/blob/3.6/Lib/pathlib.py
  - Docs: https://docs.python.org/3/library/pathlib.html

- pathpy

  - Source: https://github.com/jaraco/path.py/blob/master/path.py
  - Source: https://github.com/jaraco/path.py
  - Docs: https://pathpy.readthedocs.io/en/latest/

Sets
++++

attr table
==========

================== == ======= ====== ======= =======
attr               os os.path shutil pathlib path.py 
================== == ======= ====== ======= =======
`__div__`_                                    X      
`__rdiv__`_                                   X      
`absolute`_                          X               
`abspath`_            X                       X      
`access`_          X                          X      
`altsep`_          X  X                              
`anchor`_                            X               
`as_posix`_                          X               
`as_uri`_                            X               
`atime`_                                      X      
`basename`_           X                       X      
`bytes`_                                      X      
`capitalize`_                                 X      
`casefold`_                                   X      
`cd`_                                         X      
`center`_                                     X      
`chdir`_           X                          X      
`chmod`_           X                 X        X      
`chown`_           X          X               X      
`chroot`_          X                          X      
`chunks`_                                     X      
`commonpath`_         X                              
`commonprefix`_       X                              
`copy`_                       X               X      
`copy2`_                      X               X      
`copyfile`_                   X               X      
`copymode`_                   X               X      
`copystat`_                   X               X      
`copytree`_                   X               X      
`count`_                                      X      
`ctime`_                                      X      
`curdir`_          X  X                              
`cwd`_                               X               
`defpath`_         X  X                              
`devnull`_         X  X                              
`dirname`_            X                       X      
`dirs`_                                       X      
`drive`_                             X        X      
`encode`_                                     X      
`endswith`_                                   X      
`exists`_             X              X        X      
`expand`_                                     X      
`expandtabs`_                                 X      
`expanduser`_         X              X        X      
`expandvars`_         X                       X      
`ext`_                                        X      
`extsep`_          X  X                              
`files`_                                      X      
`find`_                                       X      
`fnmatch`_                    X               X      
`format`_                                     X      
`format_map`_                                 X      
`get_owner`_                                  X      
`getatime`_           X                       X      
`getctime`_           X                       X      
`getcwd`_          X                          X      
`getmtime`_           X                       X      
`getsize`_            X                       X      
`glob`_                              X        X      
`group`_                             X               
`home`_                              X               
`in_place`_                                   X      
`index`_                                      X      
`is_absolute`_                       X               
`is_block_device`_                   X               
`is_char_device`_                    X               
`is_dir`_                            X               
`is_fifo`_                           X               
`is_file`_                           X               
`is_reserved`_                       X               
`is_socket`_                         X               
`is_symlink`_                        X               
`isabs`_              X                       X      
`isalnum`_                                    X      
`isalpha`_                                    X      
`isdecimal`_                                  X      
`isdigit`_                                    X      
`isdir`_              X                       X      
`isfile`_             X                       X      
`isidentifier`_                               X      
`islink`_             X                       X      
`islower`_                                    X      
`ismount`_            X                       X      
`isnumeric`_                                  X      
`isprintable`_                                X      
`isspace`_                                    X      
`istitle`_                                    X      
`isupper`_                                    X      
`iterdir`_                           X               
`join`_               X                       X      
`joinpath`_                          X        X      
`lchmod`_                            X               
`lexists`_            X                              
`lines`_                                      X      
`link`_            X                          X      
`listdir`_         X                          X      
`ljust`_                                      X      
`lower`_                                      X      
`lstat`_           X                 X        X      
`lstrip`_                                     X      
`makedirs`_        X                          X      
`makedirs_p`_                                 X      
`maketrans`_                                  X      
`match`_                             X               
`merge_tree`_                                 X      
`mkdir`_           X                 X        X      
`mkdir_p`_                                    X      
`module`_                                     X      
`move`_                       X               X      
`mtime`_                                      X      
`name`_            X                 X        X      
`namebase`_                                   X      
`normcase`_           X                       X      
`normpath`_           X                       X      
`open`_            X                 X        X      
`os`_                 X       X                      
`owner`_                             X        X      
`pardir`_          X  X                              
`parent`_                            X        X      
`parents`_                           X               
`partition`_                                  X      
`parts`_                             X               
`pathconf`_        X                          X      
`pathsep`_         X  X                              
`read_bytes`_                        X               
`read_hash`_                                  X      
`read_hexhash`_                               X      
`read_md5`_                                   X      
`read_text`_                         X               
`readlink`_        X                          X      
`readlinkabs`_                                X      
`realpath`_           X                       X      
`relative_to`_                       X               
`relpath`_            X                       X      
`relpathto`_                                  X      
`remove`_          X                          X      
`remove_p`_                                   X      
`removedirs`_      X                          X      
`removedirs_p`_                               X      
`rename`_          X                 X        X      
`renames`_         X                          X      
`replace`_         X                 X        X      
`resolve`_                           X               
`rfind`_                                      X      
`rglob`_                             X               
`rindex`_                                     X      
`rjust`_                                      X      
`rmdir`_           X                 X        X      
`rmdir_p`_                                    X      
`rmtree`_                     X               X      
`rmtree_p`_                                   X      
`root`_                              X               
`rpartition`_                                 X      
`rsplit`_                                     X      
`rstrip`_                                     X      
`samefile`_           X              X        X      
`sameopenfile`_       X                              
`samestat`_           X                              
`sep`_             X  X                              
`size`_                                       X      
`special`_                                    X      
`split`_              X                       X      
`splitall`_                                   X      
`splitdrive`_         X                       X      
`splitext`_           X                       X      
`splitlines`_                                 X      
`splitpath`_                                  X      
`splitunc`_                                   X      
`startswith`_                                 X      
`stat`_            X  X       X      X        X      
`statvfs`_         X                          X      
`stem`_                              X        X      
`strip`_                                      X      
`stripext`_                                   X      
`suffix`_                            X               
`suffixes`_                          X               
`swapcase`_                                   X      
`symlink`_         X                          X      
`symlink_to`_                        X               
`text`_                                       X      
`title`_                                      X      
`touch`_                             X        X      
`translate`_                                  X      
`uncshare`_                                   X      
`unlink`_          X                 X        X      
`unlink_p`_                                   X      
`upper`_                                      X      
`using_module`_                               X      
`utime`_           X                          X      
`walk`_            X                          X      
`walkdirs`_                                   X      
`walkfiles`_                                  X      
`with_name`_                         X               
`with_suffix`_                       X        X      
`write_bytes`_                       X        X      
`write_lines`_                                X      
`write_text`_                        X        X      
`zfill`_                                      X      
================== == ======= ====== ======= =======

pathlib_and_pathpy
==================
- `chmod`_
- `drive`_
- `exists`_
- `expanduser`_
- `glob`_
- `joinpath`_
- `lstat`_
- `mkdir`_
- `name`_
- `open`_
- `owner`_
- `parent`_
- `rename`_
- `replace`_
- `rmdir`_
- `samefile`_
- `stat`_
- `stem`_
- `touch`_
- `unlink`_
- `with_suffix`_
- `write_bytes`_
- `write_text`_

pathlib_not_pathpy
==================
- `absolute`_
- `anchor`_
- `as_posix`_
- `as_uri`_
- `cwd`_
- `group`_
- `home`_
- `is_absolute`_
- `is_block_device`_
- `is_char_device`_
- `is_dir`_
- `is_fifo`_
- `is_file`_
- `is_reserved`_
- `is_socket`_
- `is_symlink`_
- `iterdir`_
- `lchmod`_
- `match`_
- `parents`_
- `parts`_
- `read_bytes`_
- `read_text`_
- `relative_to`_
- `resolve`_
- `rglob`_
- `root`_
- `suffix`_
- `suffixes`_
- `symlink_to`_
- `with_name`_

pathpy_not_pathlib
==================
- `__div__`_
- `__rdiv__`_
- `abspath`_
- `access`_
- `atime`_
- `basename`_
- `bytes`_
- `capitalize`_
- `casefold`_
- `cd`_
- `center`_
- `chdir`_
- `chown`_
- `chroot`_
- `chunks`_
- `copy`_
- `copy2`_
- `copyfile`_
- `copymode`_
- `copystat`_
- `copytree`_
- `count`_
- `ctime`_
- `dirname`_
- `dirs`_
- `encode`_
- `endswith`_
- `expand`_
- `expandtabs`_
- `expandvars`_
- `ext`_
- `files`_
- `find`_
- `fnmatch`_
- `format`_
- `format_map`_
- `get_owner`_
- `getatime`_
- `getctime`_
- `getcwd`_
- `getmtime`_
- `getsize`_
- `in_place`_
- `index`_
- `isabs`_
- `isalnum`_
- `isalpha`_
- `isdecimal`_
- `isdigit`_
- `isdir`_
- `isfile`_
- `isidentifier`_
- `islink`_
- `islower`_
- `ismount`_
- `isnumeric`_
- `isprintable`_
- `isspace`_
- `istitle`_
- `isupper`_
- `join`_
- `lines`_
- `link`_
- `listdir`_
- `ljust`_
- `lower`_
- `lstrip`_
- `makedirs`_
- `makedirs_p`_
- `maketrans`_
- `merge_tree`_
- `mkdir_p`_
- `module`_
- `move`_
- `mtime`_
- `namebase`_
- `normcase`_
- `normpath`_
- `partition`_
- `pathconf`_
- `read_hash`_
- `read_hexhash`_
- `read_md5`_
- `readlink`_
- `readlinkabs`_
- `realpath`_
- `relpath`_
- `relpathto`_
- `remove`_
- `remove_p`_
- `removedirs`_
- `removedirs_p`_
- `renames`_
- `rfind`_
- `rindex`_
- `rjust`_
- `rmdir_p`_
- `rmtree`_
- `rmtree_p`_
- `rpartition`_
- `rsplit`_
- `rstrip`_
- `size`_
- `special`_
- `split`_
- `splitall`_
- `splitdrive`_
- `splitext`_
- `splitlines`_
- `splitpath`_
- `splitunc`_
- `startswith`_
- `statvfs`_
- `strip`_
- `stripext`_
- `swapcase`_
- `symlink`_
- `text`_
- `title`_
- `translate`_
- `uncshare`_
- `unlink_p`_
- `upper`_
- `using_module`_
- `utime`_
- `walk`_
- `walkdirs`_
- `walkfiles`_
- `write_lines`_
- `zfill`_


attrs
+++++

``__div__``
============
| **pathpy.__div__**\ ``(self, rel)``

| **pathpy.__div__**\ ``(self, rel)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.__div__>`__

.. code:: python

        def __div__(self, rel):
            """ fp.__div__(rel) == fp / rel == fp.joinpath(rel)

            Join two path components, adding a separator character if
            needed.

            .. seealso:: :func:`os.path.join`
            """
            return self._next_class(self.module.join(self, rel))



``__rdiv__``
=============
| **pathpy.__rdiv__**\ ``(self, rel)``

| **pathpy.__rdiv__**\ ``(self, rel)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.__rdiv__>`__

.. code:: python

        def __rdiv__(self, rel):
            """ fp.__rdiv__(rel) == rel / fp

            Join two path components, adding a separator character if
            needed.

            .. seealso:: :func:`os.path.join`
            """
            return self._next_class(self.module.join(rel, self))



``absolute``
=============
| **pathlib.absolute**\ ``(self)``

| seealso: `pathlib.is_absolute <#is-absolute>`_
 
| **pathlib.absolute**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute>`__

.. code:: python

        def absolute(self):
            """Return an absolute version of this path.  This function works
            even if the path doesn't point to anything.

            No normalization is done, i.e. all '.' and '..' will be kept along.
            Use resolve() to get the canonical path to a file.
            """
            # XXX untested yet!
            if self._closed:
                self._raise_closed()
            if self.is_absolute():
                return self
            # FIXME this must defer to the specific flavour (and, under Windows,
            # use nt._getfullpathname())
            obj = self._from_parts([os.getcwd()] + self._parts, init=False)
            obj._init(template=self)
            return obj



``abspath``
============
| **os.path.abspath**\ ``(path)``
| **pathpy.abspath**\ ``(self)``

| **os.path.abspath**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.abspath>`__

.. code:: python

    def abspath(path):
        """Return an absolute path."""
        path = os.fspath(path)
        if not isabs(path):
            if isinstance(path, bytes):
                cwd = os.getcwdb()
            else:
                cwd = os.getcwd()
            path = join(cwd, path)
        return normpath(path)


| **pathpy.abspath**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.abspath>`__

.. code:: python

        def abspath(self):
            """ .. seealso:: :func:`os.path.abspath` """
            return self._next_class(self.module.abspath(self))



``access``
===========
| **os.access**\ ``(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)``
| **pathpy.access**\ ``(self, mode)``

| **os.access**\ ``(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.access>`__

.. code:: python

    Use the real uid/gid to test for access to a path.

      path
        Path to be tested; can be string or bytes
      mode
        Operating-system mode bitfield.  Can be F_OK to test existence,
        or the inclusive-OR of R_OK, W_OK, and X_OK.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      effective_ids
        If True, access will use the effective uid/gid instead of
        the real uid/gid.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        access will examine the symbolic link itself instead of the file
        the link points to.

    dir_fd, effective_ids, and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.

    Note that most operations will use the effective uid/gid, therefore this
      routine can be used in a suid/sgid environment to test if the invoking user
      has the specified access to the path.

| **pathpy.access**\ ``(self, mode)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.access>`__

.. code:: python

            def access(self, mode):
                """ Return ``True`` if current user has access to this path.

                mode - One of the constants :data:`os.F_OK`, :data:`os.R_OK`,
                :data:`os.W_OK`, :data:`os.X_OK`

                .. seealso:: :func:`os.access`
                """
                return os.access(self, mode)



``altsep``
===========

| **os.altsep**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.altsep>`__
| **os.path.altsep**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.altsep>`__

``anchor``
===========

| **pathlib.anchor**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.anchor>`__

.. code:: python

    The concatenation of the drive and root, or ''.


``as_posix``
=============
| **pathlib.as_posix**\ ``(self)``

| **pathlib.as_posix**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.as_posix>`__

.. code:: python

        def as_posix(self):
            """Return the string representation of the path with forward (/)
            slashes."""
            f = self._flavour
            return str(self).replace(f.sep, '/')



``as_uri``
===========
| **pathlib.as_uri**\ ``(self)``

| **pathlib.as_uri**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.as_uri>`__

.. code:: python

        def as_uri(self):
            """Return the path as a 'file' URI."""
            if not self.is_absolute():
                raise ValueError("relative path can't be expressed as a file URI")
            return self._flavour.make_uri(self)



``atime``
==========

| seealso: `pathpy.getatime <#getatime>`_, `os.path.getatime <#getatime>`_
 
| **pathpy.atime**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.atime>`__

.. code:: python

    Last access time of the file.

    .. seealso:: :meth:`getatime`, :func:`os.path.getatime`


``basename``
=============
| **os.path.basename**\ ``(p)``
| **pathpy.basename**\ ``(self)``

| **os.path.basename**\ ``(p)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.basename>`__

.. code:: python

    def basename(p):
        """Returns the final component of a pathname"""
        p = os.fspath(p)
        sep = _get_sep(p)
        i = p.rfind(sep) + 1
        return p[i:]


| **pathpy.basename**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.basename>`__

.. code:: python

        def basename(self):
            """ .. seealso:: :attr:`name`, :func:`os.path.basename` """
            return self._next_class(self.module.basename(self))



``bytes``
==========
| **pathpy.bytes**\ ``(self)``

| **pathpy.bytes**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.bytes>`__

.. code:: python

        def bytes(self):
            """ Open this file, read all bytes, return them as a string. """
            with self.open('rb') as f:
                return f.read()



``capitalize``
===============

| **pathpy.capitalize**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.capitalize>`__

.. code:: python

    S.capitalize() -> str

    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.


``casefold``
=============

| **pathpy.casefold**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.casefold>`__

.. code:: python

    S.casefold() -> str

    Return a version of S suitable for caseless comparisons.


``cd``
=======
| **pathpy.cd**\ ``(self)``

| **pathpy.cd**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.cd>`__

.. code:: python

        def chdir(self):
            """ .. seealso:: :func:`os.chdir` """
            os.chdir(self)



``center``
===========

| **pathpy.center**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.center>`__

.. code:: python

    S.center(width[, fillchar]) -> str

    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)


``chdir``
==========
| **os.chdir**\ ``(path)``
| **pathpy.chdir**\ ``(self)``

| **os.chdir**\ ``(path)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.chdir>`__

.. code:: python

    Change the current working directory to the specified path.

    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.

| **pathpy.chdir**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.chdir>`__

.. code:: python

        def chdir(self):
            """ .. seealso:: :func:`os.chdir` """
            os.chdir(self)



``chmod``
==========
| **os.chmod**\ ``(path, mode, *, dir_fd=None, follow_symlinks=True)``
| **pathlib.chmod**\ ``(self, mode)``
| **pathpy.chmod**\ ``(self, mode)``

| **os.chmod**\ ``(path, mode, *, dir_fd=None, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.chmod>`__

.. code:: python

    Change the access permissions of a file.

      path
        Path to be modified.  May always be specified as a str or bytes.
        On some platforms, path may also be specified as an open file descriptor.
        If this functionality is unavailable, using it raises an exception.
      mode
        Operating-system mode bitfield.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        chmod will modify the symbolic link itself instead of the file
        the link points to.

    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.

| **pathlib.chmod**\ ``(self, mode)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod>`__

.. code:: python

        def chmod(self, mode):
            """
            Change the permissions of the path, like os.chmod().
            """
            if self._closed:
                self._raise_closed()
            self._accessor.chmod(self, mode)


| **pathpy.chmod**\ ``(self, mode)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.chmod>`__

.. code:: python

        def chmod(self, mode):
            """
            Set the mode. May be the new mode (os.chmod behavior) or a `symbolic
            mode <http://en.wikipedia.org/wiki/Chmod#Symbolic_modes>`_.

            .. seealso:: :func:`os.chmod`
            """
            if isinstance(mode, string_types):
                mask = _multi_permission_mask(mode)
                mode = mask(self.stat().st_mode)
            os.chmod(self, mode)
            return self



``chown``
==========
| **os.chown**\ ``(path, uid, gid, *, dir_fd=None, follow_symlinks=True)``
| **shutil.chown**\ ``(path, user=None, group=None)``
| **pathpy.chown**\ ``(self, uid=-1, gid=-1)``

| **os.chown**\ ``(path, uid, gid, *, dir_fd=None, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.chown>`__

.. code:: python

    Change the owner and group id of path to the numeric uid and gid.\

      path
        Path to be examined; can be string, bytes, or open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.

    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, chown will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.

| **shutil.chown**\ ``(path, user=None, group=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.chown>`__

.. code:: python

    def chown(path, user=None, group=None):
        """Change owner user and group of the given path.

        user and group can be the uid/gid or the user/group names, and in that case,
        they are converted to their respective uid/gid.
        """

        if user is None and group is None:
            raise ValueError("user and/or group must be set")

        _user = user
        _group = group

        # -1 means don't change it
        if user is None:
            _user = -1
        # user can either be an int (the uid) or a string (the system username)
        elif isinstance(user, str):
            _user = _get_uid(user)
            if _user is None:
                raise LookupError("no such user: {!r}".format(user))

        if group is None:
            _group = -1
        elif not isinstance(group, int):
            _group = _get_gid(group)
            if _group is None:
                raise LookupError("no such group: {!r}".format(group))

        os.chown(path, _user, _group)


| **pathpy.chown**\ ``(self, uid=-1, gid=-1)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.chown>`__

.. code:: python

        def chown(self, uid=-1, gid=-1):
            """
            Change the owner and group by names rather than the uid or gid numbers.

            .. seealso:: :func:`os.chown`
            """
            if hasattr(os, 'chown'):
                if 'pwd' in globals() and isinstance(uid, string_types):
                    uid = pwd.getpwnam(uid).pw_uid
                if 'grp' in globals() and isinstance(gid, string_types):
                    gid = grp.getgrnam(gid).gr_gid
                os.chown(self, uid, gid)
            else:
                msg = "Ownership not available on this platform."
                raise NotImplementedError(msg)
            return self



``chroot``
===========
| **os.chroot**\ ``(path)``
| **pathpy.chroot**\ ``(self)``

| **os.chroot**\ ``(path)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.chroot>`__

.. code:: python

    Change root directory to path.

| **pathpy.chroot**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.chroot>`__

.. code:: python

            def chroot(self):
                """ .. seealso:: :func:`os.chroot` """
                os.chroot(self)



``chunks``
===========
| **pathpy.chunks**\ ``(self, size, *args, **kwargs)``

| **pathpy.chunks**\ ``(self, size, *args, **kwargs)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.chunks>`__

.. code:: python

        def chunks(self, size, *args, **kwargs):
            """ Returns a generator yielding chunks of the file, so it can
                be read piece by piece with a simple for loop.

               Any argument you pass after `size` will be passed to :meth:`open`.

               :example:

                   >>> hash = hashlib.md5()
                   >>> for chunk in Path("path.py").chunks(8192, mode='rb'):
                   ...     hash.update(chunk)

                This will read the file by chunks of 8192 bytes.
            """
            with self.open(*args, **kwargs) as f:
                for chunk in iter(lambda: f.read(size) or None, None):
                    yield chunk



``commonpath``
===============
| **os.path.commonpath**\ ``(paths)``

| **os.path.commonpath**\ ``(paths)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.commonpath>`__

.. code:: python

    def commonpath(paths):
        """Given a sequence of path names, returns the longest common sub-path."""

        if not paths:
            raise ValueError('commonpath() arg is an empty sequence')

        paths = tuple(map(os.fspath, paths))
        if isinstance(paths[0], bytes):
            sep = b'/'
            curdir = b'.'
        else:
            sep = '/'
            curdir = '.'

        try:
            split_paths = [path.split(sep) for path in paths]

            try:
                isabs, = set(p[:1] == sep for p in paths)
            except ValueError:
                raise ValueError("Can't mix absolute and relative paths") from None

            split_paths = [[c for c in s if c and c != curdir] for s in split_paths]
            s1 = min(split_paths)
            s2 = max(split_paths)
            common = s1
            for i, c in enumerate(s1):
                if c != s2[i]:
                    common = s1[:i]
                    break

            prefix = sep if isabs else sep[:0]
            return prefix + sep.join(common)
        except (TypeError, AttributeError):
            genericpath._check_arg_types('commonpath', *paths)
            raise



``commonprefix``
=================
| **os.path.commonprefix**\ ``(m)``

| **os.path.commonprefix**\ ``(m)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.commonprefix>`__

.. code:: python

    def commonprefix(m):
        "Given a list of pathnames, returns the longest common leading component"
        if not m: return ''
        # Some people pass in a list of pathname parts to operate in an OS-agnostic
        # fashion; don't try to translate in that case as that's an abuse of the
        # API and they are already doing what they need to be OS-agnostic and so
        # they most likely won't be using an os.PathLike object in the sublists.
        if not isinstance(m[0], (list, tuple)):
            m = tuple(map(os.fspath, m))
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1



``copy``
=========
| **shutil.copy**\ ``(src, dst, *, follow_symlinks=True)``
| **pathpy.copy**\ ``(src, dst, *, follow_symlinks=True)``

| **shutil.copy**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.copy>`__

.. code:: python

    def copy(src, dst, *, follow_symlinks=True):
        """Copy data and mode bits ("cp src dst"). Return the file's destination.

        The destination may be a directory.

        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".

        If source and destination are the same file, a SameFileError will be
        raised.

        """
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        copyfile(src, dst, follow_symlinks=follow_symlinks)
        copymode(src, dst, follow_symlinks=follow_symlinks)
        return dst


| **pathpy.copy**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.copy>`__

.. code:: python

    def copy(src, dst, *, follow_symlinks=True):
        """Copy data and mode bits ("cp src dst"). Return the file's destination.

        The destination may be a directory.

        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".

        If source and destination are the same file, a SameFileError will be
        raised.

        """
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        copyfile(src, dst, follow_symlinks=follow_symlinks)
        copymode(src, dst, follow_symlinks=follow_symlinks)
        return dst



``copy2``
==========
| **shutil.copy2**\ ``(src, dst, *, follow_symlinks=True)``
| **pathpy.copy2**\ ``(src, dst, *, follow_symlinks=True)``

| **shutil.copy2**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.copy2>`__

.. code:: python

    def copy2(src, dst, *, follow_symlinks=True):
        """Copy data and all stat info ("cp -p src dst"). Return the file's
        destination."

        The destination may be a directory.

        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".

        """
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        copyfile(src, dst, follow_symlinks=follow_symlinks)
        copystat(src, dst, follow_symlinks=follow_symlinks)
        return dst


| **pathpy.copy2**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.copy2>`__

.. code:: python

    def copy2(src, dst, *, follow_symlinks=True):
        """Copy data and all stat info ("cp -p src dst"). Return the file's
        destination."

        The destination may be a directory.

        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".

        """
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        copyfile(src, dst, follow_symlinks=follow_symlinks)
        copystat(src, dst, follow_symlinks=follow_symlinks)
        return dst



``copyfile``
=============
| **shutil.copyfile**\ ``(src, dst, *, follow_symlinks=True)``
| **pathpy.copyfile**\ ``(src, dst, *, follow_symlinks=True)``

| **shutil.copyfile**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.copyfile>`__

.. code:: python

    def copyfile(src, dst, *, follow_symlinks=True):
        """Copy data from src to dst.

        If follow_symlinks is not set and src is a symbolic link, a new
        symlink will be created instead of copying the file it points to.

        """
        if _samefile(src, dst):
            raise SameFileError("{!r} and {!r} are the same file".format(src, dst))

        for fn in [src, dst]:
            try:
                st = os.stat(fn)
            except OSError:
                # File most likely does not exist
                pass
            else:
                # XXX What about other special files? (sockets, devices...)
                if stat.S_ISFIFO(st.st_mode):
                    raise SpecialFileError("`%s` is a named pipe" % fn)

        if not follow_symlinks and os.path.islink(src):
            os.symlink(os.readlink(src), dst)
        else:
            with open(src, 'rb') as fsrc:
                with open(dst, 'wb') as fdst:
                    copyfileobj(fsrc, fdst)
        return dst


| **pathpy.copyfile**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.copyfile>`__

.. code:: python

    def copyfile(src, dst, *, follow_symlinks=True):
        """Copy data from src to dst.

        If follow_symlinks is not set and src is a symbolic link, a new
        symlink will be created instead of copying the file it points to.

        """
        if _samefile(src, dst):
            raise SameFileError("{!r} and {!r} are the same file".format(src, dst))

        for fn in [src, dst]:
            try:
                st = os.stat(fn)
            except OSError:
                # File most likely does not exist
                pass
            else:
                # XXX What about other special files? (sockets, devices...)
                if stat.S_ISFIFO(st.st_mode):
                    raise SpecialFileError("`%s` is a named pipe" % fn)

        if not follow_symlinks and os.path.islink(src):
            os.symlink(os.readlink(src), dst)
        else:
            with open(src, 'rb') as fsrc:
                with open(dst, 'wb') as fdst:
                    copyfileobj(fsrc, fdst)
        return dst



``copymode``
=============
| **shutil.copymode**\ ``(src, dst, *, follow_symlinks=True)``
| **pathpy.copymode**\ ``(src, dst, *, follow_symlinks=True)``

| **shutil.copymode**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.copymode>`__

.. code:: python

    def copymode(src, dst, *, follow_symlinks=True):
        """Copy mode bits from src to dst.

        If follow_symlinks is not set, symlinks aren't followed if and only
        if both `src` and `dst` are symlinks.  If `lchmod` isn't available
        (e.g. Linux) this method does nothing.

        """
        if not follow_symlinks and os.path.islink(src) and os.path.islink(dst):
            if hasattr(os, 'lchmod'):
                stat_func, chmod_func = os.lstat, os.lchmod
            else:
                return
        elif hasattr(os, 'chmod'):
            stat_func, chmod_func = os.stat, os.chmod
        else:
            return

        st = stat_func(src)
        chmod_func(dst, stat.S_IMODE(st.st_mode))


| **pathpy.copymode**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.copymode>`__

.. code:: python

    def copymode(src, dst, *, follow_symlinks=True):
        """Copy mode bits from src to dst.

        If follow_symlinks is not set, symlinks aren't followed if and only
        if both `src` and `dst` are symlinks.  If `lchmod` isn't available
        (e.g. Linux) this method does nothing.

        """
        if not follow_symlinks and os.path.islink(src) and os.path.islink(dst):
            if hasattr(os, 'lchmod'):
                stat_func, chmod_func = os.lstat, os.lchmod
            else:
                return
        elif hasattr(os, 'chmod'):
            stat_func, chmod_func = os.stat, os.chmod
        else:
            return

        st = stat_func(src)
        chmod_func(dst, stat.S_IMODE(st.st_mode))



``copystat``
=============
| **shutil.copystat**\ ``(src, dst, *, follow_symlinks=True)``
| **pathpy.copystat**\ ``(src, dst, *, follow_symlinks=True)``

| **shutil.copystat**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.copystat>`__

.. code:: python

    def copystat(src, dst, *, follow_symlinks=True):
        """Copy all stat info (mode bits, atime, mtime, flags) from src to dst.

        If the optional flag `follow_symlinks` is not set, symlinks aren't followed if and
        only if both `src` and `dst` are symlinks.

        """
        def _nop(*args, ns=None, follow_symlinks=None):
            pass

        # follow symlinks (aka don't not follow symlinks)
        follow = follow_symlinks or not (os.path.islink(src) and os.path.islink(dst))
        if follow:
            # use the real function if it exists
            def lookup(name):
                return getattr(os, name, _nop)
        else:
            # use the real function only if it exists
            # *and* it supports follow_symlinks
            def lookup(name):
                fn = getattr(os, name, _nop)
                if fn in os.supports_follow_symlinks:
                    return fn
                return _nop

        st = lookup("stat")(src, follow_symlinks=follow)
        mode = stat.S_IMODE(st.st_mode)
        lookup("utime")(dst, ns=(st.st_atime_ns, st.st_mtime_ns),
            follow_symlinks=follow)
        try:
            lookup("chmod")(dst, mode, follow_symlinks=follow)
        except NotImplementedError:
            # if we got a NotImplementedError, it's because
            #   * follow_symlinks=False,
            #   * lchown() is unavailable, and
            #   * either
            #       * fchownat() is unavailable or
            #       * fchownat() doesn't implement AT_SYMLINK_NOFOLLOW.
            #         (it returned ENOSUP.)
            # therefore we're out of options--we simply cannot chown the
            # symlink.  give up, suppress the error.
            # (which is what shutil always did in this circumstance.)
            pass
        if hasattr(st, 'st_flags'):
            try:
                lookup("chflags")(dst, st.st_flags, follow_symlinks=follow)
            except OSError as why:
                for err in 'EOPNOTSUPP', 'ENOTSUP':
                    if hasattr(errno, err) and why.errno == getattr(errno, err):
                        break
                else:
                    raise
        _copyxattr(src, dst, follow_symlinks=follow)


| **pathpy.copystat**\ ``(src, dst, *, follow_symlinks=True)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.copystat>`__

.. code:: python

    def copystat(src, dst, *, follow_symlinks=True):
        """Copy all stat info (mode bits, atime, mtime, flags) from src to dst.

        If the optional flag `follow_symlinks` is not set, symlinks aren't followed if and
        only if both `src` and `dst` are symlinks.

        """
        def _nop(*args, ns=None, follow_symlinks=None):
            pass

        # follow symlinks (aka don't not follow symlinks)
        follow = follow_symlinks or not (os.path.islink(src) and os.path.islink(dst))
        if follow:
            # use the real function if it exists
            def lookup(name):
                return getattr(os, name, _nop)
        else:
            # use the real function only if it exists
            # *and* it supports follow_symlinks
            def lookup(name):
                fn = getattr(os, name, _nop)
                if fn in os.supports_follow_symlinks:
                    return fn
                return _nop

        st = lookup("stat")(src, follow_symlinks=follow)
        mode = stat.S_IMODE(st.st_mode)
        lookup("utime")(dst, ns=(st.st_atime_ns, st.st_mtime_ns),
            follow_symlinks=follow)
        try:
            lookup("chmod")(dst, mode, follow_symlinks=follow)
        except NotImplementedError:
            # if we got a NotImplementedError, it's because
            #   * follow_symlinks=False,
            #   * lchown() is unavailable, and
            #   * either
            #       * fchownat() is unavailable or
            #       * fchownat() doesn't implement AT_SYMLINK_NOFOLLOW.
            #         (it returned ENOSUP.)
            # therefore we're out of options--we simply cannot chown the
            # symlink.  give up, suppress the error.
            # (which is what shutil always did in this circumstance.)
            pass
        if hasattr(st, 'st_flags'):
            try:
                lookup("chflags")(dst, st.st_flags, follow_symlinks=follow)
            except OSError as why:
                for err in 'EOPNOTSUPP', 'ENOTSUP':
                    if hasattr(errno, err) and why.errno == getattr(errno, err):
                        break
                else:
                    raise
        _copyxattr(src, dst, follow_symlinks=follow)



``copytree``
=============
| **shutil.copytree**\ ``(src, dst, symlinks=False, ignore=None, copy_function=<function copy2 at 0x7f41d2964488>, ignore_dangling_symlinks=False)``
| **pathpy.copytree**\ ``(src, dst, symlinks=False, ignore=None, copy_function=<function copy2 at 0x7f41d2964488>, ignore_dangling_symlinks=False)``

| **shutil.copytree**\ ``(src, dst, symlinks=False, ignore=None, copy_function=<function copy2 at 0x7f41d2964488>, ignore_dangling_symlinks=False)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.copytree>`__

.. code:: python

    def copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,
                 ignore_dangling_symlinks=False):
        """Recursively copy a directory tree.

        The destination directory must not already exist.
        If exception(s) occur, an Error is raised with a list of reasons.

        If the optional symlinks flag is true, symbolic links in the
        source tree result in symbolic links in the destination tree; if
        it is false, the contents of the files pointed to by symbolic
        links are copied. If the file pointed by the symlink doesn't
        exist, an exception will be added in the list of errors raised in
        an Error exception at the end of the copy process.

        You can set the optional ignore_dangling_symlinks flag to true if you
        want to silence this exception. Notice that this has no effect on
        platforms that don't support os.symlink.

        The optional ignore argument is a callable. If given, it
        is called with the `src` parameter, which is the directory
        being visited by copytree(), and `names` which is the list of
        `src` contents, as returned by os.listdir():

            callable(src, names) -> ignored_names

        Since copytree() is called recursively, the callable will be
        called once for each directory that is copied. It returns a
        list of names relative to the `src` directory that should
        not be copied.

        The optional copy_function argument is a callable that will be used
        to copy each file. It will be called with the source path and the
        destination path as arguments. By default, copy2() is used, but any
        function that supports the same signature (like copy()) can be used.

        """
        names = os.listdir(src)
        if ignore is not None:
            ignored_names = ignore(src, names)
        else:
            ignored_names = set()

        os.makedirs(dst)
        errors = []
        for name in names:
            if name in ignored_names:
                continue
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    if symlinks:
                        # We can't just leave it to `copy_function` because legacy
                        # code with a custom `copy_function` may rely on copytree
                        # doing the right thing.
                        os.symlink(linkto, dstname)
                        copystat(srcname, dstname, follow_symlinks=not symlinks)
                    else:
                        # ignore dangling symlink if the flag is on
                        if not os.path.exists(linkto) and ignore_dangling_symlinks:
                            continue
                        # otherwise let the copy occurs. copy2 will raise an error
                        if os.path.isdir(srcname):
                            copytree(srcname, dstname, symlinks, ignore,
                                     copy_function)
                        else:
                            copy_function(srcname, dstname)
                elif os.path.isdir(srcname):
                    copytree(srcname, dstname, symlinks, ignore, copy_function)
                else:
                    # Will raise a SpecialFileError for unsupported file types
                    copy_function(srcname, dstname)
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except Error as err:
                errors.extend(err.args[0])
            except OSError as why:
                errors.append((srcname, dstname, str(why)))
        try:
            copystat(src, dst)
        except OSError as why:
            # Copying file access times may fail on Windows
            if getattr(why, 'winerror', None) is None:
                errors.append((src, dst, str(why)))
        if errors:
            raise Error(errors)
        return dst


| **pathpy.copytree**\ ``(src, dst, symlinks=False, ignore=None, copy_function=<function copy2 at 0x7f41d2964488>, ignore_dangling_symlinks=False)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.copytree>`__

.. code:: python

    def copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,
                 ignore_dangling_symlinks=False):
        """Recursively copy a directory tree.

        The destination directory must not already exist.
        If exception(s) occur, an Error is raised with a list of reasons.

        If the optional symlinks flag is true, symbolic links in the
        source tree result in symbolic links in the destination tree; if
        it is false, the contents of the files pointed to by symbolic
        links are copied. If the file pointed by the symlink doesn't
        exist, an exception will be added in the list of errors raised in
        an Error exception at the end of the copy process.

        You can set the optional ignore_dangling_symlinks flag to true if you
        want to silence this exception. Notice that this has no effect on
        platforms that don't support os.symlink.

        The optional ignore argument is a callable. If given, it
        is called with the `src` parameter, which is the directory
        being visited by copytree(), and `names` which is the list of
        `src` contents, as returned by os.listdir():

            callable(src, names) -> ignored_names

        Since copytree() is called recursively, the callable will be
        called once for each directory that is copied. It returns a
        list of names relative to the `src` directory that should
        not be copied.

        The optional copy_function argument is a callable that will be used
        to copy each file. It will be called with the source path and the
        destination path as arguments. By default, copy2() is used, but any
        function that supports the same signature (like copy()) can be used.

        """
        names = os.listdir(src)
        if ignore is not None:
            ignored_names = ignore(src, names)
        else:
            ignored_names = set()

        os.makedirs(dst)
        errors = []
        for name in names:
            if name in ignored_names:
                continue
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    if symlinks:
                        # We can't just leave it to `copy_function` because legacy
                        # code with a custom `copy_function` may rely on copytree
                        # doing the right thing.
                        os.symlink(linkto, dstname)
                        copystat(srcname, dstname, follow_symlinks=not symlinks)
                    else:
                        # ignore dangling symlink if the flag is on
                        if not os.path.exists(linkto) and ignore_dangling_symlinks:
                            continue
                        # otherwise let the copy occurs. copy2 will raise an error
                        if os.path.isdir(srcname):
                            copytree(srcname, dstname, symlinks, ignore,
                                     copy_function)
                        else:
                            copy_function(srcname, dstname)
                elif os.path.isdir(srcname):
                    copytree(srcname, dstname, symlinks, ignore, copy_function)
                else:
                    # Will raise a SpecialFileError for unsupported file types
                    copy_function(srcname, dstname)
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except Error as err:
                errors.extend(err.args[0])
            except OSError as why:
                errors.append((srcname, dstname, str(why)))
        try:
            copystat(src, dst)
        except OSError as why:
            # Copying file access times may fail on Windows
            if getattr(why, 'winerror', None) is None:
                errors.append((src, dst, str(why)))
        if errors:
            raise Error(errors)
        return dst



``count``
==========

| **pathpy.count**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.count>`__

.. code:: python

    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.


``ctime``
==========

| seealso: `pathpy.getctime <#getctime>`_, `os.path.getctime <#getctime>`_
 
| **pathpy.ctime**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.ctime>`__

.. code:: python

    Creation time of the file.

    .. seealso:: :meth:`getctime`, :func:`os.path.getctime`


``curdir``
===========

| **os.curdir**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.curdir>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **os.path.curdir**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.curdir>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.


``cwd``
========
| **pathlib.cwd**\ ``()``

| seealso: `pathpy.getcwd <#getcwd>`_, `os.getcwd <#getcwd>`_
 
| **pathlib.cwd**\ ``()``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd>`__

.. code:: python

        @classmethod
        def cwd(cls):
            """Return a new path pointing to the current working directory
            (as returned by os.getcwd()).
            """
            return cls(os.getcwd())



``defpath``
============

| **os.defpath**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.defpath>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **os.path.defpath**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.defpath>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.


``devnull``
============

| **os.devnull**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.devnull>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **os.path.devnull**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.devnull>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.


``dirname``
============
| **os.path.dirname**\ ``(p)``
| **pathpy.dirname**\ ``(self)``

| **os.path.dirname**\ ``(p)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.dirname>`__

.. code:: python

    def dirname(p):
        """Returns the directory component of a pathname"""
        p = os.fspath(p)
        sep = _get_sep(p)
        i = p.rfind(sep) + 1
        head = p[:i]
        if head and head != sep*len(head):
            head = head.rstrip(sep)
        return head


| **pathpy.dirname**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.dirname>`__

.. code:: python

        def dirname(self):
            """ .. seealso:: :attr:`parent`, :func:`os.path.dirname` """
            return self._next_class(self.module.dirname(self))



``dirs``
=========
| **pathpy.dirs**\ ``(self, pattern=None)``

| **pathpy.dirs**\ ``(self, pattern=None)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.dirs>`__

.. code:: python

        def dirs(self, pattern=None):
            """ D.dirs() -> List of this directory's subdirectories.

            The elements of the list are Path objects.
            This does not walk recursively into subdirectories
            (but see :meth:`walkdirs`).

            With the optional `pattern` argument, this only lists
            directories whose names match the given pattern.  For
            example, ``d.dirs('build-*')``.
            """
            return [p for p in self.listdir(pattern) if p.isdir()]



``drive``
==========

| **pathlib.drive**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.drive>`__

.. code:: python

    The drive prefix (letter or UNC path), if any.

| **pathpy.drive**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.drive>`__

.. code:: python

    The drive specifier, for example ``'C:'``.

    This is always empty on systems that don't use drive specifiers.


``encode``
===========

| **pathpy.encode**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.encode>`__

.. code:: python

    S.encode(encoding='utf-8', errors='strict') -> bytes

    Encode S using the codec registered for encoding. Default encoding
    is 'utf-8'. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.


``endswith``
=============

| **pathpy.endswith**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.endswith>`__

.. code:: python

    S.endswith(suffix[, start[, end]]) -> bool

    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.


``exists``
===========
| **os.path.exists**\ ``(path)``
| **pathlib.exists**\ ``(self)``
| **pathpy.exists**\ ``(self)``

| **os.path.exists**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.exists>`__

.. code:: python

    def exists(path):
        """Test whether a path exists.  Returns False for broken symbolic links"""
        try:
            os.stat(path)
        except OSError:
            return False
        return True


| **pathlib.exists**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists>`__

.. code:: python

        def exists(self):
            """
            Whether this path exists.
            """
            try:
                self.stat()
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                return False
            return True


| **pathpy.exists**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.exists>`__

.. code:: python

        def exists(self):
            """ .. seealso:: :func:`os.path.exists` """
            return self.module.exists(self)



``expand``
===========
| **pathpy.expand**\ ``(self)``

| **pathpy.expand**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.expand>`__

.. code:: python

        def expand(self):
            """ Clean up a filename by calling :meth:`expandvars()`,
            :meth:`expanduser()`, and :meth:`normpath()` on it.

            This is commonly everything needed to clean up a filename
            read from a configuration file, for example.
            """
            return self.expandvars().expanduser().normpath()



``expandtabs``
===============

| **pathpy.expandtabs**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.expandtabs>`__

.. code:: python

    S.expandtabs(tabsize=8) -> str

    Return a copy of S where all tab characters are expanded using spaces.
    If tabsize is not given, a tab size of 8 characters is assumed.


``expanduser``
===============
| **os.path.expanduser**\ ``(path)``
| **pathlib.expanduser**\ ``(self)``
| **pathpy.expanduser**\ ``(self)``

| **os.path.expanduser**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.expanduser>`__

.. code:: python

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
        path = os.fspath(path)
        if isinstance(path, bytes):
            tilde = b'~'
        else:
            tilde = '~'
        if not path.startswith(tilde):
            return path
        sep = _get_sep(path)
        i = path.find(sep, 1)
        if i < 0:
            i = len(path)
        if i == 1:
            if 'HOME' not in os.environ:
                import pwd
                userhome = pwd.getpwuid(os.getuid()).pw_dir
            else:
                userhome = os.environ['HOME']
        else:
            import pwd
            name = path[1:i]
            if isinstance(name, bytes):
                name = str(name, 'ASCII')
            try:
                pwent = pwd.getpwnam(name)
            except KeyError:
                return path
            userhome = pwent.pw_dir
        if isinstance(path, bytes):
            userhome = os.fsencode(userhome)
            root = b'/'
        else:
            root = '/'
        userhome = userhome.rstrip(root)
        return (userhome + path[i:]) or root


| **pathlib.expanduser**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser>`__

.. code:: python

        def expanduser(self):
            """ Return a new path with expanded ~ and ~user constructs
            (as returned by os.path.expanduser)
            """
            if (not (self._drv or self._root) and
                self._parts and self._parts[0][:1] == '~'):
                homedir = self._flavour.gethomedir(self._parts[0][1:])
                return self._from_parts([homedir] + self._parts[1:])

            return self


| **pathpy.expanduser**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.expanduser>`__

.. code:: python

        def expanduser(self):
            """ .. seealso:: :func:`os.path.expanduser` """
            return self._next_class(self.module.expanduser(self))



``expandvars``
===============
| **os.path.expandvars**\ ``(path)``
| **pathpy.expandvars**\ ``(self)``

| **os.path.expandvars**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.expandvars>`__

.. code:: python

    def expandvars(path):
        """Expand shell variables of form $var and ${var}.  Unknown variables
        are left unchanged."""
        path = os.fspath(path)
        global _varprog, _varprogb
        if isinstance(path, bytes):
            if b'$' not in path:
                return path
            if not _varprogb:
                import re
                _varprogb = re.compile(br'\$(\w+|\{[^}]*\})', re.ASCII)
            search = _varprogb.search
            start = b'{'
            end = b'}'
            environ = getattr(os, 'environb', None)
        else:
            if '$' not in path:
                return path
            if not _varprog:
                import re
                _varprog = re.compile(r'\$(\w+|\{[^}]*\})', re.ASCII)
            search = _varprog.search
            start = '{'
            end = '}'
            environ = os.environ
        i = 0
        while True:
            m = search(path, i)
            if not m:
                break
            i, j = m.span(0)
            name = m.group(1)
            if name.startswith(start) and name.endswith(end):
                name = name[1:-1]
            try:
                if environ is None:
                    value = os.fsencode(os.environ[os.fsdecode(name)])
                else:
                    value = environ[name]
            except KeyError:
                i = j
            else:
                tail = path[j:]
                path = path[:i] + value
                i = len(path)
                path += tail
        return path


| **pathpy.expandvars**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.expandvars>`__

.. code:: python

        def expandvars(self):
            """ .. seealso:: :func:`os.path.expandvars` """
            return self._next_class(self.module.expandvars(self))



``ext``
========

| **pathpy.ext**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.ext>`__

.. code:: python

    The file extension, for example ``'.py'``. 


``extsep``
===========

| **os.extsep**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.extsep>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **os.path.extsep**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.extsep>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.


``files``
==========
| **pathpy.files**\ ``(self, pattern=None)``

| **pathpy.files**\ ``(self, pattern=None)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.files>`__

.. code:: python

        def files(self, pattern=None):
            """ D.files() -> List of the files in this directory.

            The elements of the list are Path objects.
            This does not walk into subdirectories (see :meth:`walkfiles`).

            With the optional `pattern` argument, this only lists files
            whose names match the given pattern.  For example,
            ``d.files('*.pyc')``.
            """

            return [p for p in self.listdir(pattern) if p.isfile()]



``find``
=========

| **pathpy.find**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.find>`__

.. code:: python

    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.


``fnmatch``
============
| **pathpy.fnmatch**\ ``(self, pattern, normcase=None)``

| **shutil.fnmatch**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.fnmatch>`__

.. code:: python

    Filename matching with shell patterns.

    fnmatch(FILENAME, PATTERN) matches according to the local convention.
    fnmatchcase(FILENAME, PATTERN) always takes case in account.

    The functions operate by translating the pattern into a regular
    expression.  They cache the compiled regular expressions for speed.

    The function translate(PATTERN) returns a regular expression
    corresponding to PATTERN.  (It does not compile it.)

| **pathpy.fnmatch**\ ``(self, pattern, normcase=None)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.fnmatch>`__

.. code:: python

        def fnmatch(self, pattern, normcase=None):
            """ Return ``True`` if `self.name` matches the given `pattern`.

            `pattern` - A filename pattern with wildcards,
                for example ``'*.py'``. If the pattern contains a `normcase`
                attribute, it is applied to the name and path prior to comparison.

            `normcase` - (optional) A function used to normalize the pattern and
                filename before matching. Defaults to :meth:`self.module`, which
                defaults to :meth:`os.path.normcase`.

            .. seealso:: :func:`fnmatch.fnmatch`
            """
            default_normcase = getattr(pattern, 'normcase', self.module.normcase)
            normcase = normcase or default_normcase
            name = normcase(self.name)
            pattern = normcase(pattern)
            return fnmatch.fnmatchcase(name, pattern)



``format``
===========

| **pathpy.format**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.format>`__

.. code:: python

    S.format(*args, **kwargs) -> str

    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').


``format_map``
===============

| **pathpy.format_map**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.format_map>`__

.. code:: python

    S.format_map(mapping) -> str

    Return a formatted version of S, using substitutions from mapping.
    The substitutions are identified by braces ('{' and '}').


``get_owner``
==============
| **pathpy.get_owner**\ ``(self)``

| seealso: `pathlib.owner <#owner>`_
 
| **pathpy.get_owner**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.get_owner>`__

.. code:: python

        def __get_owner_unix(self):
            """
            Return the name of the owner of this file or directory. Follow
            symbolic links.

            .. seealso:: :attr:`owner`
            """
            st = self.stat()
            return pwd.getpwuid(st.st_uid).pw_name



``getatime``
=============
| **os.path.getatime**\ ``(filename)``
| **pathpy.getatime**\ ``(self)``

| seealso: `pathlib.atime <#atime>`_
 
| **os.path.getatime**\ ``(filename)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.getatime>`__

.. code:: python

    def getatime(filename):
        """Return the last access time of a file, reported by os.stat()."""
        return os.stat(filename).st_atime


| **pathpy.getatime**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.getatime>`__

.. code:: python

        def getatime(self):
            """ .. seealso:: :attr:`atime`, :func:`os.path.getatime` """
            return self.module.getatime(self)



``getctime``
=============
| **os.path.getctime**\ ``(filename)``
| **pathpy.getctime**\ ``(self)``

| seealso: `pathlib.ctime <#ctime>`_
 
| **os.path.getctime**\ ``(filename)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.getctime>`__

.. code:: python

    def getctime(filename):
        """Return the metadata change time of a file, reported by os.stat()."""
        return os.stat(filename).st_ctime


| **pathpy.getctime**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.getctime>`__

.. code:: python

        def getctime(self):
            """ .. seealso:: :attr:`ctime`, :func:`os.path.getctime` """
            return self.module.getctime(self)



``getcwd``
===========
| **os.getcwd**\ ``()``
| **pathpy.getcwd**\ ``()``

| seealso: `pathlib.cwd <#cwd>`_
 
| **os.getcwd**\ ``()``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.getcwd>`__

.. code:: python

    Return a unicode string representing the current working directory.

| **pathpy.getcwd**\ ``()``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.getcwd>`__

.. code:: python

        @classmethod
        def getcwd(cls):
            """ Return the current working directory as a path object.

            .. seealso:: :func:`os.getcwdu`
            """
            return cls(getcwdu())



``getmtime``
=============
| **os.path.getmtime**\ ``(filename)``
| **pathpy.getmtime**\ ``(self)``

| seealso: `pathlib.mtime <#mtime>`_
 
| **os.path.getmtime**\ ``(filename)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.getmtime>`__

.. code:: python

    def getmtime(filename):
        """Return the last modification time of a file, reported by os.stat()."""
        return os.stat(filename).st_mtime


| **pathpy.getmtime**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.getmtime>`__

.. code:: python

        def getmtime(self):
            """ .. seealso:: :attr:`mtime`, :func:`os.path.getmtime` """
            return self.module.getmtime(self)



``getsize``
============
| **os.path.getsize**\ ``(filename)``
| **pathpy.getsize**\ ``(self)``

| seealso: `pathpy.size <#size>`_
 
| **os.path.getsize**\ ``(filename)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.getsize>`__

.. code:: python

    def getsize(filename):
        """Return the size of a file, reported by os.stat()."""
        return os.stat(filename).st_size


| **pathpy.getsize**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.getsize>`__

.. code:: python

        def getsize(self):
            """ .. seealso:: :attr:`size`, :func:`os.path.getsize` """
            return self.module.getsize(self)



``glob``
=========
| **pathlib.glob**\ ``(self, pattern)``
| **pathpy.glob**\ ``(self, pattern)``

| **pathlib.glob**\ ``(self, pattern)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob>`__

.. code:: python

        def glob(self, pattern):
            """Iterate over this subtree and yield all existing files (of any
            kind, including directories) matching the given pattern.
            """
            if not pattern:
                raise ValueError("Unacceptable pattern: {!r}".format(pattern))
            pattern = self._flavour.casefold(pattern)
            drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
            if drv or root:
                raise NotImplementedError("Non-relative patterns are unsupported")
            selector = _make_selector(tuple(pattern_parts))
            for p in selector.select_from(self):
                yield p


| **pathpy.glob**\ ``(self, pattern)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.glob>`__

.. code:: python

        def glob(self, pattern):
            """ Return a list of Path objects that match the pattern.

            `pattern` - a path relative to this directory, with wildcards.

            For example, ``Path('/users').glob('*/bin/*')`` returns a list
            of all the files users have in their :file:`bin` directories.

            .. seealso:: :func:`glob.glob`
            """
            cls = self._next_class
            return [cls(s) for s in glob.glob(self / pattern)]



``group``
==========
| **pathlib.group**\ ``(self)``

| **pathlib.group**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.group>`__

.. code:: python

        def group(self):
            """
            Return the group name of the file gid.
            """
            import grp
            return grp.getgrgid(self.stat().st_gid).gr_name



``home``
=========
| **pathlib.home**\ ``()``

| **pathlib.home**\ ``()``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.home>`__

.. code:: python

        @classmethod
        def home(cls):
            """Return a new path pointing to the user's home directory (as
            returned by os.path.expanduser('~')).
            """
            return cls(cls()._flavour.gethomedir(None))



``in_place``
=============
| **pathpy.in_place**\ ``(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None, backup_extension=None)``

| **pathpy.in_place**\ ``(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None, backup_extension=None)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.in_place>`__

.. code:: python

        @contextlib.contextmanager
        def in_place(
                self, mode='r', buffering=-1, encoding=None, errors=None,
                newline=None, backup_extension=None,
        ):
            """
            A context in which a file may be re-written in-place with
            new content.

            Yields a tuple of :samp:`({readable}, {writable})` file
            objects, where `writable` replaces `readable`.

            If an exception occurs, the old file is restored, removing the
            written data.

            Mode *must not* use ``'w'``, ``'a'``, or ``'+'``; only
            read-only-modes are allowed. A :exc:`ValueError` is raised
            on invalid modes.

            For example, to add line numbers to a file::

                p = Path(filename)
                assert p.isfile()
                with p.in_place() as (reader, writer):
                    for number, line in enumerate(reader, 1):
                        writer.write('{0:3}: '.format(number)))
                        writer.write(line)

            Thereafter, the file at `filename` will have line numbers in it.
            """
            import io

            if set(mode).intersection('wa+'):
                raise ValueError('Only read-only file modes can be used')

            # move existing file to backup, create new file with same permissions
            # borrowed extensively from the fileinput module
            backup_fn = self + (backup_extension or os.extsep + 'bak')
            try:
                os.unlink(backup_fn)
            except os.error:
                pass
            os.rename(self, backup_fn)
            readable = io.open(
                backup_fn, mode, buffering=buffering,
                encoding=encoding, errors=errors, newline=newline,
            )
            try:
                perm = os.fstat(readable.fileno()).st_mode
            except OSError:
                writable = open(
                    self, 'w' + mode.replace('r', ''),
                    buffering=buffering, encoding=encoding, errors=errors,
                    newline=newline,
                )
            else:
                os_mode = os.O_CREAT | os.O_WRONLY | os.O_TRUNC
                if hasattr(os, 'O_BINARY'):
                    os_mode |= os.O_BINARY
                fd = os.open(self, os_mode, perm)
                writable = io.open(
                    fd, "w" + mode.replace('r', ''),
                    buffering=buffering, encoding=encoding, errors=errors,
                    newline=newline,
                )
                try:
                    if hasattr(os, 'chmod'):
                        os.chmod(self, perm)
                except OSError:
                    pass
            try:
                yield readable, writable
            except Exception:
                # move backup back
                readable.close()
                writable.close()
                try:
                    os.unlink(self)
                except os.error:
                    pass
                os.rename(backup_fn, self)
                raise
            else:
                readable.close()
                writable.close()
            finally:
                try:
                    os.unlink(backup_fn)
                except os.error:
                    pass



``index``
==========

| **pathpy.index**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.index>`__

.. code:: python

    S.index(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found, 
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Raises ValueError when the substring is not found.


``is_absolute``
================
| **pathlib.is_absolute**\ ``(self)``

| seealso: `pathlib.absolute <#absolute>`_, `pathpy.isabs <#isabs>`_, `os.path.isabs <#isabs>`_
 
| **pathlib.is_absolute**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_absolute>`__

.. code:: python

        def is_absolute(self):
            """True if the path is absolute (has both a root and, if applicable,
            a drive)."""
            if not self._root:
                return False
            return not self._flavour.has_drv or bool(self._drv)



``is_block_device``
====================
| **pathlib.is_block_device**\ ``(self)``

| **pathlib.is_block_device**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_block_device>`__

.. code:: python

        def is_block_device(self):
            """
            Whether this path is a block device.
            """
            try:
                return S_ISBLK(self.stat().st_mode)
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                # Path doesn't exist or is a broken symlink
                # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
                return False



``is_char_device``
===================
| **pathlib.is_char_device**\ ``(self)``

| **pathlib.is_char_device**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_char_device>`__

.. code:: python

        def is_char_device(self):
            """
            Whether this path is a character device.
            """
            try:
                return S_ISCHR(self.stat().st_mode)
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                # Path doesn't exist or is a broken symlink
                # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
                return False



``is_dir``
===========
| **pathlib.is_dir**\ ``(self)``

| seealso: `pathpy.isdir <#isdir>`_, `os.path.isdir <#isdir>`_
 
| **pathlib.is_dir**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir>`__

.. code:: python

        def is_dir(self):
            """
            Whether this path is a directory.
            """
            try:
                return S_ISDIR(self.stat().st_mode)
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                # Path doesn't exist or is a broken symlink
                # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
                return False



``is_fifo``
============
| **pathlib.is_fifo**\ ``(self)``

| **pathlib.is_fifo**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_fifo>`__

.. code:: python

        def is_fifo(self):
            """
            Whether this path is a FIFO.
            """
            try:
                return S_ISFIFO(self.stat().st_mode)
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                # Path doesn't exist or is a broken symlink
                # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
                return False



``is_file``
============
| **pathlib.is_file**\ ``(self)``

| seealso: `pathpy.isfile <#isfile>`_, `os.path.isfile <#isfile>`_
 
| **pathlib.is_file**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file>`__

.. code:: python

        def is_file(self):
            """
            Whether this path is a regular file (also True for symlinks pointing
            to regular files).
            """
            try:
                return S_ISREG(self.stat().st_mode)
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                # Path doesn't exist or is a broken symlink
                # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
                return False



``is_reserved``
================
| **pathlib.is_reserved**\ ``(self)``

| **pathlib.is_reserved**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_reserved>`__

.. code:: python

        def is_reserved(self):
            """Return True if the path contains one of the special names reserved
            by the system, if any."""
            return self._flavour.is_reserved(self._parts)



``is_socket``
==============
| **pathlib.is_socket**\ ``(self)``

| **pathlib.is_socket**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_socket>`__

.. code:: python

        def is_socket(self):
            """
            Whether this path is a socket.
            """
            try:
                return S_ISSOCK(self.stat().st_mode)
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                # Path doesn't exist or is a broken symlink
                # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
                return False



``is_symlink``
===============
| **pathlib.is_symlink**\ ``(self)``

| seealso: `pathpy.islink <#islink>`_, `os.path.islink <#islink>`_
 
| **pathlib.is_symlink**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_symlink>`__

.. code:: python

        def is_symlink(self):
            """
            Whether this path is a symbolic link.
            """
            try:
                return S_ISLNK(self.lstat().st_mode)
            except OSError as e:
                if e.errno not in (ENOENT, ENOTDIR):
                    raise
                # Path doesn't exist
                return False



``isabs``
==========
| **os.path.isabs**\ ``(s)``
| **pathpy.isabs**\ ``(self)``

| seealso: `pathlib.is_absolute <#is-absolute>`_
 
| **os.path.isabs**\ ``(s)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.isabs>`__

.. code:: python

    def isabs(s):
        """Test whether a path is absolute"""
        s = os.fspath(s)
        sep = _get_sep(s)
        return s.startswith(sep)


| **pathpy.isabs**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isabs>`__

.. code:: python

        def isabs(self):
            """ .. seealso:: :func:`os.path.isabs` """
            return self.module.isabs(self)



``isalnum``
============

| **pathpy.isalnum**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isalnum>`__

.. code:: python

    S.isalnum() -> bool

    Return True if all characters in S are alphanumeric
    and there is at least one character in S, False otherwise.


``isalpha``
============

| **pathpy.isalpha**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isalpha>`__

.. code:: python

    S.isalpha() -> bool

    Return True if all characters in S are alphabetic
    and there is at least one character in S, False otherwise.


``isdecimal``
==============

| **pathpy.isdecimal**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isdecimal>`__

.. code:: python

    S.isdecimal() -> bool

    Return True if there are only decimal characters in S,
    False otherwise.


``isdigit``
============

| **pathpy.isdigit**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isdigit>`__

.. code:: python

    S.isdigit() -> bool

    Return True if all characters in S are digits
    and there is at least one character in S, False otherwise.


``isdir``
==========
| **os.path.isdir**\ ``(s)``
| **pathpy.isdir**\ ``(self)``

| seealso: `pathlib.is_dir <#is-dir>`_
 
| **os.path.isdir**\ ``(s)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.isdir>`__

.. code:: python

    def isdir(s):
        """Return true if the pathname refers to an existing directory."""
        try:
            st = os.stat(s)
        except OSError:
            return False
        return stat.S_ISDIR(st.st_mode)


| **pathpy.isdir**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isdir>`__

.. code:: python

        def isdir(self):
            """ .. seealso:: :func:`os.path.isdir` """
            return self.module.isdir(self)



``isfile``
===========
| **os.path.isfile**\ ``(path)``
| **pathpy.isfile**\ ``(self)``

| seealso: `pathlib.is_file <#is-file>`_
 
| **os.path.isfile**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.isfile>`__

.. code:: python

    def isfile(path):
        """Test whether a path is a regular file"""
        try:
            st = os.stat(path)
        except OSError:
            return False
        return stat.S_ISREG(st.st_mode)


| **pathpy.isfile**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isfile>`__

.. code:: python

        def isfile(self):
            """ .. seealso:: :func:`os.path.isfile` """
            return self.module.isfile(self)



``isidentifier``
=================

| **pathpy.isidentifier**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isidentifier>`__

.. code:: python

    S.isidentifier() -> bool

    Return True if S is a valid identifier according
    to the language definition.

    Use keyword.iskeyword() to test for reserved identifiers
    such as "def" and "class".


``islink``
===========
| **os.path.islink**\ ``(path)``
| **pathpy.islink**\ ``(self)``

| seealso: `pathlib.is_symlink <#is-symlink>`_
 
| **os.path.islink**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.islink>`__

.. code:: python

    def islink(path):
        """Test whether a path is a symbolic link"""
        try:
            st = os.lstat(path)
        except (OSError, AttributeError):
            return False
        return stat.S_ISLNK(st.st_mode)


| **pathpy.islink**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.islink>`__

.. code:: python

        def islink(self):
            """ .. seealso:: :func:`os.path.islink` """
            return self.module.islink(self)



``islower``
============

| **pathpy.islower**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.islower>`__

.. code:: python

    S.islower() -> bool

    Return True if all cased characters in S are lowercase and there is
    at least one cased character in S, False otherwise.


``ismount``
============
| **os.path.ismount**\ ``(path)``
| **pathpy.ismount**\ ``(self)``

| **os.path.ismount**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.ismount>`__

.. code:: python

    def ismount(path):
        """Test whether a path is a mount point"""
        try:
            s1 = os.lstat(path)
        except OSError:
            # It doesn't exist -- so not a mount point. :-)
            return False
        else:
            # A symlink can never be a mount point
            if stat.S_ISLNK(s1.st_mode):
                return False

        if isinstance(path, bytes):
            parent = join(path, b'..')
        else:
            parent = join(path, '..')
        parent = realpath(parent)
        try:
            s2 = os.lstat(parent)
        except OSError:
            return False

        dev1 = s1.st_dev
        dev2 = s2.st_dev
        if dev1 != dev2:
            return True     # path/.. on a different device as path
        ino1 = s1.st_ino
        ino2 = s2.st_ino
        if ino1 == ino2:
            return True     # path/.. is the same i-node as path
        return False


| **pathpy.ismount**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.ismount>`__

.. code:: python

        def ismount(self):
            """ .. seealso:: :func:`os.path.ismount` """
            return self.module.ismount(self)



``isnumeric``
==============

| **pathpy.isnumeric**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isnumeric>`__

.. code:: python

    S.isnumeric() -> bool

    Return True if there are only numeric characters in S,
    False otherwise.


``isprintable``
================

| **pathpy.isprintable**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isprintable>`__

.. code:: python

    S.isprintable() -> bool

    Return True if all characters in S are considered
    printable in repr() or S is empty, False otherwise.


``isspace``
============

| **pathpy.isspace**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isspace>`__

.. code:: python

    S.isspace() -> bool

    Return True if all characters in S are whitespace
    and there is at least one character in S, False otherwise.


``istitle``
============

| **pathpy.istitle**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.istitle>`__

.. code:: python

    S.istitle() -> bool

    Return True if S is a titlecased string and there is at least one
    character in S, i.e. upper- and titlecase characters may only
    follow uncased characters and lowercase characters only cased ones.
    Return False otherwise.


``isupper``
============

| **pathpy.isupper**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.isupper>`__

.. code:: python

    S.isupper() -> bool

    Return True if all cased characters in S are uppercase and there is
    at least one cased character in S, False otherwise.


``iterdir``
============
| **pathlib.iterdir**\ ``(self)``

| seealso: `pathpy.listdir <#listdir>`_
 
| **pathlib.iterdir**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir>`__

.. code:: python

        def iterdir(self):
            """Iterate over the files in this directory.  Does not yield any
            result for the special paths '.' and '..'.
            """
            if self._closed:
                self._raise_closed()
            for name in self._accessor.listdir(self):
                if name in {'.', '..'}:
                    # Yielding a path object for these makes little sense
                    continue
                yield self._make_child_relpath(name)
                if self._closed:
                    self._raise_closed()



``join``
=========
| **os.path.join**\ ``(a, *p)``

| seealso: `pathlib.joinpath <#joinpath>`_
 
| **os.path.join**\ ``(a, *p)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.join>`__

.. code:: python

    def join(a, *p):
        """Join two or more pathname components, inserting '/' as needed.
        If any component is an absolute path, all previous path components
        will be discarded.  An empty last part will result in a path that
        ends with a separator."""
        a = os.fspath(a)
        sep = _get_sep(a)
        path = a
        try:
            if not p:
                path[:0] + sep  #23780: Ensure compatible data type even if p is null.
            for b in map(os.fspath, p):
                if b.startswith(sep):
                    path = b
                elif not path or path.endswith(sep):
                    path += b
                else:
                    path += sep + b
        except (TypeError, AttributeError, BytesWarning):
            genericpath._check_arg_types('join', a, *p)
            raise
        return path


| **pathpy.join**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.join>`__

.. code:: python

    S.join(iterable) -> str

    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.


``joinpath``
=============
| **pathlib.joinpath**\ ``(self, *args)``
| **pathpy.joinpath**\ ``(first, *others)``

| seealso: `os.path.join <#join>`_
 
| **pathlib.joinpath**\ ``(self, *args)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.joinpath>`__

.. code:: python

        def joinpath(self, *args):
            """Combine this path with one or several arguments, and return a
            new path representing either a subpath (if all arguments are relative
            paths) or a totally different path (if one of the arguments is
            anchored).
            """
            return self._make_child(args)


| **pathpy.joinpath**\ ``(first, *others)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.joinpath>`__

.. code:: python

    partial(func, *args, **keywords) - new function with partial application
    of the given arguments and keywords.


``lchmod``
===========
| **pathlib.lchmod**\ ``(self, mode)``

| **pathlib.lchmod**\ ``(self, mode)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.lchmod>`__

.. code:: python

        def lchmod(self, mode):
            """
            Like chmod(), except if the path points to a symlink, the symlink's
            permissions are changed, rather than its target's.
            """
            if self._closed:
                self._raise_closed()
            self._accessor.lchmod(self, mode)



``lexists``
============
| **os.path.lexists**\ ``(path)``

| **os.path.lexists**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.lexists>`__

.. code:: python

    def lexists(path):
        """Test whether a path exists.  Returns True for broken symbolic links"""
        try:
            os.lstat(path)
        except OSError:
            return False
        return True



``lines``
==========
| **pathpy.lines**\ ``(self, encoding=None, errors='strict', retain=True)``

| **pathpy.lines**\ ``(self, encoding=None, errors='strict', retain=True)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.lines>`__

.. code:: python

        def lines(self, encoding=None, errors='strict', retain=True):
            r""" Open this file, read all lines, return them in a list.

            Optional arguments:
                `encoding` - The Unicode encoding (or character set) of
                    the file.  The default is ``None``, meaning the content
                    of the file is read as 8-bit characters and returned
                    as a list of (non-Unicode) str objects.
                `errors` - How to handle Unicode errors; see help(str.decode)
                    for the options.  Default is ``'strict'``.
                `retain` - If ``True``, retain newline characters; but all newline
                    character combinations (``'\r'``, ``'\n'``, ``'\r\n'``) are
                    translated to ``'\n'``.  If ``False``, newline characters are
                    stripped off.  Default is ``True``.

            This uses ``'U'`` mode.

            .. seealso:: :meth:`text`
            """
            if encoding is None and retain:
                with self.open('U') as f:
                    return f.readlines()
            else:
                return self.text(encoding, errors).splitlines(retain)



``link``
=========
| **os.link**\ ``(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)``
| **pathpy.link**\ ``(self, newpath)``

| **os.link**\ ``(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.link>`__

.. code:: python

    Create a hard link to a file.

    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    If follow_symlinks is False, and the last element of src is a symbolic
      link, link will create a link to the symbolic link itself instead of the
      file the link points to.
    src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
      platform.  If they are unavailable, using them will raise a
      NotImplementedError.

| **pathpy.link**\ ``(self, newpath)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.link>`__

.. code:: python

            def link(self, newpath):
                """ Create a hard link at `newpath`, pointing to this file.

                .. seealso:: :func:`os.link`
                """
                os.link(self, newpath)
                return self._next_class(newpath)



``listdir``
============
| **os.listdir**\ ``(path=None)``
| **pathpy.listdir**\ ``(self, pattern=None)``

| seealso: `pathlib.iterdir <#iterdir>`_
 
| **os.listdir**\ ``(path=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.listdir>`__

.. code:: python

    Return a list containing the names of the files in the directory.

    path can be specified as either str or bytes.  If path is bytes,
      the filenames returned will also be bytes; in all other circumstances
      the filenames returned will be str.
    If path is None, uses the path='.'.
    On some platforms, path may also be specified as an open file descriptor;\
      the file descriptor must refer to a directory.
      If this functionality is unavailable, using it raises NotImplementedError.

    The list is in arbitrary order.  It does not include the special
    entries '.' and '..' even if they are present in the directory.

| **pathpy.listdir**\ ``(self, pattern=None)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.listdir>`__

.. code:: python

        def listdir(self, pattern=None):
            """ D.listdir() -> List of items in this directory.

            Use :meth:`files` or :meth:`dirs` instead if you want a listing
            of just files or just subdirectories.

            The elements of the list are Path objects.

            With the optional `pattern` argument, this only lists
            items whose names match the given pattern.

            .. seealso:: :meth:`files`, :meth:`dirs`
            """
            if pattern is None:
                pattern = '*'
            return [
                self / child
                for child in os.listdir(self)
                if self._next_class(child).fnmatch(pattern)
            ]



``ljust``
==========

| **pathpy.ljust**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.ljust>`__

.. code:: python

    S.ljust(width[, fillchar]) -> str

    Return S left-justified in a Unicode string of length width. Padding is
    done using the specified fill character (default is a space).


``lower``
==========

| **pathpy.lower**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.lower>`__

.. code:: python

    S.lower() -> str

    Return a copy of the string S converted to lowercase.


``lstat``
==========
| **os.lstat**\ ``(path, *, dir_fd=None)``
| **pathlib.lstat**\ ``(self)``
| **pathpy.lstat**\ ``(self)``

| **os.lstat**\ ``(path, *, dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.lstat>`__

.. code:: python

    Perform a stat system call on the given path, without following symbolic links.

    Like stat(), but do not follow symbolic links.
    Equivalent to stat(path, follow_symlinks=False).

| **pathlib.lstat**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.lstat>`__

.. code:: python

        def lstat(self):
            """
            Like stat(), except if the path points to a symlink, the symlink's
            status information is returned, rather than its target's.
            """
            if self._closed:
                self._raise_closed()
            return self._accessor.lstat(self)


| **pathpy.lstat**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.lstat>`__

.. code:: python

        def lstat(self):
            """ Like :meth:`stat`, but do not follow symbolic links.

            .. seealso:: :meth:`stat`, :func:`os.lstat`
            """
            return os.lstat(self)



``lstrip``
===========

| **pathpy.lstrip**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.lstrip>`__

.. code:: python

    S.lstrip([chars]) -> str

    Return a copy of the string S with leading whitespace removed.
    If chars is given and not None, remove characters in chars instead.


``makedirs``
=============
| **os.makedirs**\ ``(name, mode=511, exist_ok=False)``
| **pathpy.makedirs**\ ``(self, mode=511)``

| **os.makedirs**\ ``(name, mode=511, exist_ok=False)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.makedirs>`__

.. code:: python

    def makedirs(name, mode=0o777, exist_ok=False):
        """makedirs(name [, mode=0o777][, exist_ok=False])

        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, raise an OSError if exist_ok is False. Otherwise no exception is
        raised.  This is recursive.

        """
        head, tail = path.split(name)
        if not tail:
            head, tail = path.split(head)
        if head and tail and not path.exists(head):
            try:
                makedirs(head, mode, exist_ok)
            except FileExistsError:
                # Defeats race condition when another thread created the path
                pass
            cdir = curdir
            if isinstance(tail, bytes):
                cdir = bytes(curdir, 'ASCII')
            if tail == cdir:           # xxx/newdir/. exists if xxx/newdir exists
                return
        try:
            mkdir(name, mode)
        except OSError:
            # Cannot rely on checking for EEXIST, since the operating system
            # could give priority to other errors like EACCES or EROFS
            if not exist_ok or not path.isdir(name):
                raise


| **pathpy.makedirs**\ ``(self, mode=511)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.makedirs>`__

.. code:: python

        def makedirs(self, mode=0o777):
            """ .. seealso:: :func:`os.makedirs` """
            os.makedirs(self, mode)
            return self



``makedirs_p``
===============
| **pathpy.makedirs_p**\ ``(self, mode=511)``

| **pathpy.makedirs_p**\ ``(self, mode=511)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.makedirs_p>`__

.. code:: python

        def makedirs_p(self, mode=0o777):
            """ Like :meth:`makedirs`, but does not raise an exception if the
            directory already exists. """
            try:
                self.makedirs(mode)
            except OSError:
                _, e, _ = sys.exc_info()
                if e.errno != errno.EEXIST:
                    raise
            return self



``maketrans``
==============
| **pathpy.maketrans**\ ``(x, y=None, z=None, /)``

| **pathpy.maketrans**\ ``(x, y=None, z=None, /)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.maketrans>`__

.. code:: python

    Return a translation table usable for str.translate().

    If there is only one argument, it must be a dictionary mapping Unicode
    ordinals (integers) or characters to Unicode ordinals, strings or None.
    Character keys will be then converted to ordinals.
    If there are two arguments, they must be strings of equal length, and
    in the resulting dictionary, each character in x will be mapped to the
    character at the same position in y. If there is a third argument, it
    must be a string, whose characters will be mapped to None in the result.


``match``
==========
| **pathlib.match**\ ``(self, path_pattern)``

| **pathlib.match**\ ``(self, path_pattern)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.match>`__

.. code:: python

        def match(self, path_pattern):
            """
            Return True if this path matches the given pattern.
            """
            cf = self._flavour.casefold
            path_pattern = cf(path_pattern)
            drv, root, pat_parts = self._flavour.parse_parts((path_pattern,))
            if not pat_parts:
                raise ValueError("empty pattern")
            if drv and drv != cf(self._drv):
                return False
            if root and root != cf(self._root):
                return False
            parts = self._cparts
            if drv or root:
                if len(pat_parts) != len(parts):
                    return False
                pat_parts = pat_parts[1:]
            elif len(pat_parts) > len(parts):
                return False
            for part, pat in zip(reversed(parts), reversed(pat_parts)):
                if not fnmatch.fnmatchcase(part, pat):
                    return False
            return True



``merge_tree``
===============
| **pathpy.merge_tree**\ ``(self, dst, symlinks=False, *args, **kwargs)``

| **pathpy.merge_tree**\ ``(self, dst, symlinks=False, *args, **kwargs)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.merge_tree>`__

.. code:: python

        def merge_tree(self, dst, symlinks=False, *args, **kwargs):
            """
            Copy entire contents of self to dst, overwriting existing
            contents in dst with those in self.

            If the additional keyword `update` is True, each
            `src` will only be copied if `dst` does not exist,
            or `src` is newer than `dst`.

            Note that the technique employed stages the files in a temporary
            directory first, so this function is not suitable for merging
            trees with large files, especially if the temporary directory
            is not capable of storing a copy of the entire source tree.
            """
            update = kwargs.pop('update', False)
            with tempdir() as _temp_dir:
                # first copy the tree to a stage directory to support
                #  the parameters and behavior of copytree.
                stage = _temp_dir / str(hash(self))
                self.copytree(stage, symlinks, *args, **kwargs)
                # now copy everything from the stage directory using
                #  the semantics of dir_util.copy_tree
                distutils.dir_util.copy_tree(
                    stage,
                    dst,
                    preserve_symlinks=symlinks,
                    update=update,
                )



``mkdir``
==========
| **os.mkdir**\ ``(path, mode=511, *, dir_fd=None)``
| **pathlib.mkdir**\ ``(self, mode=511, parents=False, exist_ok=False)``
| **pathpy.mkdir**\ ``(self, mode=511)``

| **os.mkdir**\ ``(path, mode=511, *, dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.mkdir>`__

.. code:: python

    Create a directory.

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

    The mode argument is ignored on Windows.

| **pathlib.mkdir**\ ``(self, mode=511, parents=False, exist_ok=False)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir>`__

.. code:: python

        def mkdir(self, mode=0o777, parents=False, exist_ok=False):
            """
            Create a new directory at this given path.
            """
            if self._closed:
                self._raise_closed()
            try:
                self._accessor.mkdir(self, mode)
            except FileNotFoundError:
                if not parents or self.parent == self:
                    raise
                self.parent.mkdir(parents=True, exist_ok=True)
                self.mkdir(mode, parents=False, exist_ok=exist_ok)
            except OSError:
                # Cannot rely on checking for EEXIST, since the operating system
                # could give priority to other errors like EACCES or EROFS
                if not exist_ok or not self.is_dir():
                    raise


| **pathpy.mkdir**\ ``(self, mode=511)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.mkdir>`__

.. code:: python

        def mkdir(self, mode=0o777):
            """ .. seealso:: :func:`os.mkdir` """
            os.mkdir(self, mode)
            return self



``mkdir_p``
============
| **pathpy.mkdir_p**\ ``(self, mode=511)``

| **pathpy.mkdir_p**\ ``(self, mode=511)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.mkdir_p>`__

.. code:: python

        def mkdir_p(self, mode=0o777):
            """ Like :meth:`mkdir`, but does not raise an exception if the
            directory already exists. """
            try:
                self.mkdir(mode)
            except OSError:
                _, e, _ = sys.exc_info()
                if e.errno != errno.EEXIST:
                    raise
            return self



``module``
===========

| **pathpy.module**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.module>`__

.. code:: python

    Common operations on Posix pathnames.

    Instead of importing this module directly, import os and refer to
    this module as os.path.  The "os.path" name is an alias for this
    module on Posix systems; on other systems (e.g. Mac, Windows),
    os.path provides the same operations in a manner specific to that
    platform, and is an alias to another module (e.g. macpath, ntpath).

    Some of this can actually be useful on non-Posix systems too, e.g.
    for manipulation of the pathname component of URLs.


``move``
=========
| **shutil.move**\ ``(src, dst, copy_function=<function copy2 at 0x7f41d2964488>)``
| **pathpy.move**\ ``(src, dst, copy_function=<function copy2 at 0x7f41d2964488>)``

| **shutil.move**\ ``(src, dst, copy_function=<function copy2 at 0x7f41d2964488>)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.move>`__

.. code:: python

    def move(src, dst, copy_function=copy2):
        """Recursively move a file or directory to another location. This is
        similar to the Unix "mv" command. Return the file or directory's
        destination.

        If the destination is a directory or a symlink to a directory, the source
        is moved inside the directory. The destination path must not already
        exist.

        If the destination already exists but is not a directory, it may be
        overwritten depending on os.rename() semantics.

        If the destination is on our current filesystem, then rename() is used.
        Otherwise, src is copied to the destination and then removed. Symlinks are
        recreated under the new name if os.rename() fails because of cross
        filesystem renames.

        The optional `copy_function` argument is a callable that will be used
        to copy the source or it will be delegated to `copytree`.
        By default, copy2() is used, but any function that supports the same
        signature (like copy()) can be used.

        A lot more could be done here...  A look at a mv.c shows a lot of
        the issues this implementation glosses over.

        """
        real_dst = dst
        if os.path.isdir(dst):
            if _samefile(src, dst):
                # We might be on a case insensitive filesystem,
                # perform the rename anyway.
                os.rename(src, dst)
                return

            real_dst = os.path.join(dst, _basename(src))
            if os.path.exists(real_dst):
                raise Error("Destination path '%s' already exists" % real_dst)
        try:
            os.rename(src, real_dst)
        except OSError:
            if os.path.islink(src):
                linkto = os.readlink(src)
                os.symlink(linkto, real_dst)
                os.unlink(src)
            elif os.path.isdir(src):
                if _destinsrc(src, dst):
                    raise Error("Cannot move a directory '%s' into itself"
                                " '%s'." % (src, dst))
                copytree(src, real_dst, copy_function=copy_function,
                         symlinks=True)
                rmtree(src)
            else:
                copy_function(src, real_dst)
                os.unlink(src)
        return real_dst


| **pathpy.move**\ ``(src, dst, copy_function=<function copy2 at 0x7f41d2964488>)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.move>`__

.. code:: python

    def move(src, dst, copy_function=copy2):
        """Recursively move a file or directory to another location. This is
        similar to the Unix "mv" command. Return the file or directory's
        destination.

        If the destination is a directory or a symlink to a directory, the source
        is moved inside the directory. The destination path must not already
        exist.

        If the destination already exists but is not a directory, it may be
        overwritten depending on os.rename() semantics.

        If the destination is on our current filesystem, then rename() is used.
        Otherwise, src is copied to the destination and then removed. Symlinks are
        recreated under the new name if os.rename() fails because of cross
        filesystem renames.

        The optional `copy_function` argument is a callable that will be used
        to copy the source or it will be delegated to `copytree`.
        By default, copy2() is used, but any function that supports the same
        signature (like copy()) can be used.

        A lot more could be done here...  A look at a mv.c shows a lot of
        the issues this implementation glosses over.

        """
        real_dst = dst
        if os.path.isdir(dst):
            if _samefile(src, dst):
                # We might be on a case insensitive filesystem,
                # perform the rename anyway.
                os.rename(src, dst)
                return

            real_dst = os.path.join(dst, _basename(src))
            if os.path.exists(real_dst):
                raise Error("Destination path '%s' already exists" % real_dst)
        try:
            os.rename(src, real_dst)
        except OSError:
            if os.path.islink(src):
                linkto = os.readlink(src)
                os.symlink(linkto, real_dst)
                os.unlink(src)
            elif os.path.isdir(src):
                if _destinsrc(src, dst):
                    raise Error("Cannot move a directory '%s' into itself"
                                " '%s'." % (src, dst))
                copytree(src, real_dst, copy_function=copy_function,
                         symlinks=True)
                rmtree(src)
            else:
                copy_function(src, real_dst)
                os.unlink(src)
        return real_dst



``mtime``
==========

| seealso: `pathpy.getmtime <#getmtime>`_, `os.path.getmtime <#getmtime>`_
 
| **pathpy.mtime**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.mtime>`__

.. code:: python

    Last-modified time of the file.

    .. seealso:: :meth:`getmtime`, :func:`os.path.getmtime`


``name``
=========

| **os.name**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.name>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **pathlib.name**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.name>`__

.. code:: python

    The final path component, if any.

| **pathpy.name**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.name>`__

.. code:: python

    The name of this file or directory without the full path.

    For example,
    ``Path('/usr/local/lib/libpython.so').name == 'libpython.so'``

    .. seealso:: :meth:`basename`, :func:`os.path.basename`


``namebase``
=============

| **pathpy.namebase**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.namebase>`__

``normcase``
=============
| **os.path.normcase**\ ``(s)``
| **pathpy.normcase**\ ``(self)``

| **os.path.normcase**\ ``(s)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.normcase>`__

.. code:: python

    def normcase(s):
        """Normalize case of pathname.  Has no effect under Posix"""
        s = os.fspath(s)
        if not isinstance(s, (bytes, str)):
            raise TypeError("normcase() argument must be str or bytes, "
                            "not '{}'".format(s.__class__.__name__))
        return s


| **pathpy.normcase**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.normcase>`__

.. code:: python

        def normcase(self):
            """ .. seealso:: :func:`os.path.normcase` """
            return self._next_class(self.module.normcase(self))



``normpath``
=============
| **os.path.normpath**\ ``(path)``
| **pathpy.normpath**\ ``(self)``

| **os.path.normpath**\ ``(path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.normpath>`__

.. code:: python

    def normpath(path):
        """Normalize path, eliminating double slashes, etc."""
        path = os.fspath(path)
        if isinstance(path, bytes):
            sep = b'/'
            empty = b''
            dot = b'.'
            dotdot = b'..'
        else:
            sep = '/'
            empty = ''
            dot = '.'
            dotdot = '..'
        if path == empty:
            return dot
        initial_slashes = path.startswith(sep)
        # POSIX allows one or two initial slashes, but treats three or more
        # as single slash.
        if (initial_slashes and
            path.startswith(sep*2) and not path.startswith(sep*3)):
            initial_slashes = 2
        comps = path.split(sep)
        new_comps = []
        for comp in comps:
            if comp in (empty, dot):
                continue
            if (comp != dotdot or (not initial_slashes and not new_comps) or
                 (new_comps and new_comps[-1] == dotdot)):
                new_comps.append(comp)
            elif new_comps:
                new_comps.pop()
        comps = new_comps
        path = sep.join(comps)
        if initial_slashes:
            path = sep*initial_slashes + path
        return path or dot


| **pathpy.normpath**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.normpath>`__

.. code:: python

        def normpath(self):
            """ .. seealso:: :func:`os.path.normpath` """
            return self._next_class(self.module.normpath(self))



``open``
=========
| **os.open**\ ``(path, flags, mode=511, *, dir_fd=None)``
| **pathlib.open**\ ``(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None)``
| **pathpy.open**\ ``(self, *args, **kwargs)``

| **os.open**\ ``(path, flags, mode=511, *, dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.open>`__

.. code:: python

    Open a file for low level IO.  Returns a file descriptor (integer).

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

| **pathlib.open**\ ``(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.open>`__

.. code:: python

        def open(self, mode='r', buffering=-1, encoding=None,
                 errors=None, newline=None):
            """
            Open the file pointed by this path and return a file object, as
            the built-in open() function does.
            """
            if self._closed:
                self._raise_closed()
            return io.open(str(self), mode, buffering, encoding, errors, newline,
                           opener=self._opener)


| **pathpy.open**\ ``(self, *args, **kwargs)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.open>`__

.. code:: python

        def open(self, *args, **kwargs):
            """ Open this file and return a corresponding :class:`file` object.

            Keyword arguments work as in :func:`io.open`.  If the file cannot be
            opened, an :class:`~exceptions.OSError` is raised.
            """
            with io_error_compat():
                return io.open(self, *args, **kwargs)



``os``
=======

| **os.path.os**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.os>`__

.. code:: python

    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

| **shutil.os**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.os>`__

.. code:: python

    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).


``owner``
==========
| **pathlib.owner**\ ``(self)``

| seealso: `pathpy.get_owner <#get-owner>`_
 
| **pathlib.owner**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.owner>`__

.. code:: python

        def owner(self):
            """
            Return the login name of the file owner.
            """
            import pwd
            return pwd.getpwuid(self.stat().st_uid).pw_name


| **pathpy.owner**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.owner>`__

.. code:: python

    Name of the owner of this file or directory.

    .. seealso:: :meth:`get_owner`


``pardir``
===========

| **os.pardir**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.pardir>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **os.path.pardir**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.pardir>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.


``parent``
===========

| **pathlib.parent**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.parent>`__

.. code:: python

    The logical parent of the path.

| **pathpy.parent**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.parent>`__

.. code:: python

    This path's parent directory, as a new Path object.

    For example,
    ``Path('/usr/local/lib/libpython.so').parent ==
    Path('/usr/local/lib')``

    .. seealso:: :meth:`dirname`, :func:`os.path.dirname`


``parents``
============

| **pathlib.parents**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.parents>`__

.. code:: python

    A sequence of this path's logical parents.


``partition``
==============

| **pathpy.partition**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.partition>`__

.. code:: python

    S.partition(sep) -> (head, sep, tail)

    Search for the separator sep in S, and return the part before it,
    the separator itself, and the part after it.  If the separator is not
    found, return S and two empty strings.


``parts``
==========

| **pathlib.parts**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.parts>`__

.. code:: python

    An object providing sequence-like access to the
    components in the filesystem path.


``pathconf``
=============
| **os.pathconf**\ ``(path, name)``
| **pathpy.pathconf**\ ``(self, name)``

| **os.pathconf**\ ``(path, name)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.pathconf>`__

.. code:: python

    Return the configuration limit name for the file or directory path.

    If there is no limit, return -1.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.

| **pathpy.pathconf**\ ``(self, name)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.pathconf>`__

.. code:: python

            def pathconf(self, name):
                """ .. seealso:: :func:`os.pathconf` """
                return os.pathconf(self, name)



``pathsep``
============

| **os.pathsep**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.pathsep>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **os.path.pathsep**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.pathsep>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.


``read_bytes``
===============
| **pathlib.read_bytes**\ ``(self)``

| **pathlib.read_bytes**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_bytes>`__

.. code:: python

        def read_bytes(self):
            """
            Open the file in bytes mode, read it, and close the file.
            """
            with self.open(mode='rb') as f:
                return f.read()



``read_hash``
==============
| **pathpy.read_hash**\ ``(self, hash_name)``

| **pathpy.read_hash**\ ``(self, hash_name)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.read_hash>`__

.. code:: python

        def read_hash(self, hash_name):
            """ Calculate given hash for this file.

            List of supported hashes can be obtained from :mod:`hashlib` package.
            This reads the entire file.

            .. seealso:: :meth:`hashlib.hash.digest`
            """
            return self._hash(hash_name).digest()



``read_hexhash``
=================
| **pathpy.read_hexhash**\ ``(self, hash_name)``

| **pathpy.read_hexhash**\ ``(self, hash_name)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.read_hexhash>`__

.. code:: python

        def read_hexhash(self, hash_name):
            """ Calculate given hash for this file, returning hexdigest.

            List of supported hashes can be obtained from :mod:`hashlib` package.
            This reads the entire file.

            .. seealso:: :meth:`hashlib.hash.hexdigest`
            """
            return self._hash(hash_name).hexdigest()



``read_md5``
=============
| **pathpy.read_md5**\ ``(self)``

| **pathpy.read_md5**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.read_md5>`__

.. code:: python

        def read_md5(self):
            """ Calculate the md5 hash for this file.

            This reads through the entire file.

            .. seealso:: :meth:`read_hash`
            """
            return self.read_hash('md5')



``read_text``
==============
| **pathlib.read_text**\ ``(self, encoding=None, errors=None)``

| **pathlib.read_text**\ ``(self, encoding=None, errors=None)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text>`__

.. code:: python

        def read_text(self, encoding=None, errors=None):
            """
            Open the file in text mode, read it, and close the file.
            """
            with self.open(mode='r', encoding=encoding, errors=errors) as f:
                return f.read()



``readlink``
=============
| **os.readlink**\ ``<class 'builtin_function_or_method'>``
| **pathpy.readlink**\ ``(self)``

| **os.readlink**\ ``<class 'builtin_function_or_method'>``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.readlink>`__

.. code:: python

    readlink(path, *, dir_fd=None) -> path

    Return a string representing the path to which the symbolic link points.

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

| **pathpy.readlink**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.readlink>`__

.. code:: python

            def readlink(self):
                """ Return the path to which this symbolic link points.

                The result may be an absolute or a relative path.

                .. seealso:: :meth:`readlinkabs`, :func:`os.readlink`
                """
                return self._next_class(os.readlink(self))



``readlinkabs``
================
| **pathpy.readlinkabs**\ ``(self)``

| **pathpy.readlinkabs**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.readlinkabs>`__

.. code:: python

            def readlinkabs(self):
                """ Return the path to which this symbolic link points.

                The result is always an absolute path.

                .. seealso:: :meth:`readlink`, :func:`os.readlink`
                """
                p = self.readlink()
                if p.isabs():
                    return p
                else:
                    return (self.parent / p).abspath()



``realpath``
=============
| **os.path.realpath**\ ``(filename)``
| **pathpy.realpath**\ ``(self)``

| **os.path.realpath**\ ``(filename)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.realpath>`__

.. code:: python

    def realpath(filename):
        """Return the canonical path of the specified filename, eliminating any
    symbolic links encountered in the path."""
        filename = os.fspath(filename)
        path, ok = _joinrealpath(filename[:0], filename, {})
        return abspath(path)


| **pathpy.realpath**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.realpath>`__

.. code:: python

        def realpath(self):
            """ .. seealso:: :func:`os.path.realpath` """
            return self._next_class(self.module.realpath(self))



``relative_to``
================
| **pathlib.relative_to**\ ``(self, *other)``

| **pathlib.relative_to**\ ``(self, *other)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.relative_to>`__

.. code:: python

        def relative_to(self, *other):
            """Return the relative path to another path identified by the passed
            arguments.  If the operation is not possible (because this is not
            a subpath of the other path), raise ValueError.
            """
            # For the purpose of this method, drive and root are considered
            # separate parts, i.e.:
            #   Path('c:/').relative_to('c:')  gives Path('/')
            #   Path('c:/').relative_to('/')   raise ValueError
            if not other:
                raise TypeError("need at least one argument")
            parts = self._parts
            drv = self._drv
            root = self._root
            if root:
                abs_parts = [drv, root] + parts[1:]
            else:
                abs_parts = parts
            to_drv, to_root, to_parts = self._parse_args(other)
            if to_root:
                to_abs_parts = [to_drv, to_root] + to_parts[1:]
            else:
                to_abs_parts = to_parts
            n = len(to_abs_parts)
            cf = self._flavour.casefold_parts
            if (root or drv) if n == 0 else cf(abs_parts[:n]) != cf(to_abs_parts):
                formatted = self._format_parsed_parts(to_drv, to_root, to_parts)
                raise ValueError("{!r} does not start with {!r}"
                                 .format(str(self), str(formatted)))
            return self._from_parsed_parts('', root if n == 1 else '',
                                           abs_parts[n:])



``relpath``
============
| **os.path.relpath**\ ``(path, start=None)``
| **pathpy.relpath**\ ``(self, start='.')``

| **os.path.relpath**\ ``(path, start=None)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.relpath>`__

.. code:: python

    def relpath(path, start=None):
        """Return a relative version of a path"""

        if not path:
            raise ValueError("no path specified")

        path = os.fspath(path)
        if isinstance(path, bytes):
            curdir = b'.'
            sep = b'/'
            pardir = b'..'
        else:
            curdir = '.'
            sep = '/'
            pardir = '..'

        if start is None:
            start = curdir
        else:
            start = os.fspath(start)

        try:
            start_list = [x for x in abspath(start).split(sep) if x]
            path_list = [x for x in abspath(path).split(sep) if x]
            # Work out how much of the filepath is shared by start and path.
            i = len(commonprefix([start_list, path_list]))

            rel_list = [pardir] * (len(start_list)-i) + path_list[i:]
            if not rel_list:
                return curdir
            return join(*rel_list)
        except (TypeError, AttributeError, BytesWarning, DeprecationWarning):
            genericpath._check_arg_types('relpath', path, start)
            raise


| **pathpy.relpath**\ ``(self, start='.')``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.relpath>`__

.. code:: python

        def relpath(self, start='.'):
            """ Return this path as a relative path,
            based from `start`, which defaults to the current working directory.
            """
            cwd = self._next_class(start)
            return cwd.relpathto(self)



``relpathto``
==============
| **pathpy.relpathto**\ ``(self, dest)``

| **pathpy.relpathto**\ ``(self, dest)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.relpathto>`__

.. code:: python

        def relpathto(self, dest):
            """ Return a relative path from `self` to `dest`.

            If there is no relative path from `self` to `dest`, for example if
            they reside on different drives in Windows, then this returns
            ``dest.abspath()``.
            """
            origin = self.abspath()
            dest = self._next_class(dest).abspath()

            orig_list = origin.normcase().splitall()
            # Don't normcase dest!  We want to preserve the case.
            dest_list = dest.splitall()

            if orig_list[0] != self.module.normcase(dest_list[0]):
                # Can't get here from there.
                return dest

            # Find the location where the two paths start to differ.
            i = 0
            for start_seg, dest_seg in zip(orig_list, dest_list):
                if start_seg != self.module.normcase(dest_seg):
                    break
                i += 1

            # Now i is the point where the two paths diverge.
            # Need a certain number of "os.pardir"s to work up
            # from the origin to the point of divergence.
            segments = [os.pardir] * (len(orig_list) - i)
            # Need to add the diverging part of dest_list.
            segments += dest_list[i:]
            if len(segments) == 0:
                # If they happen to be identical, use os.curdir.
                relpath = os.curdir
            else:
                relpath = self.module.join(*segments)
            return self._next_class(relpath)



``remove``
===========
| **os.remove**\ ``(path, *, dir_fd=None)``
| **pathpy.remove**\ ``(self)``

| **os.remove**\ ``(path, *, dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.remove>`__

.. code:: python

    Remove a file (same as unlink()).

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

| **pathpy.remove**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.remove>`__

.. code:: python

        def remove(self):
            """ .. seealso:: :func:`os.remove` """
            os.remove(self)
            return self



``remove_p``
=============
| **pathpy.remove_p**\ ``(self)``

| **pathpy.remove_p**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.remove_p>`__

.. code:: python

        def remove_p(self):
            """ Like :meth:`remove`, but does not raise an exception if the
            file does not exist. """
            try:
                self.unlink()
            except OSError:
                _, e, _ = sys.exc_info()
                if e.errno != errno.ENOENT:
                    raise
            return self



``removedirs``
===============
| **os.removedirs**\ ``(name)``
| **pathpy.removedirs**\ ``(self)``

| **os.removedirs**\ ``(name)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.removedirs>`__

.. code:: python

    def removedirs(name):
        """removedirs(name)

        Super-rmdir; remove a leaf directory and all empty intermediate
        ones.  Works like rmdir except that, if the leaf directory is
        successfully removed, directories corresponding to rightmost path
        segments will be pruned away until either the whole path is
        consumed or an error occurs.  Errors during this latter phase are
        ignored -- they generally mean that a directory was not empty.

        """
        rmdir(name)
        head, tail = path.split(name)
        if not tail:
            head, tail = path.split(head)
        while head and tail:
            try:
                rmdir(head)
            except OSError:
                break
            head, tail = path.split(head)


| **pathpy.removedirs**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.removedirs>`__

.. code:: python

        def removedirs(self):
            """ .. seealso:: :func:`os.removedirs` """
            os.removedirs(self)
            return self



``removedirs_p``
=================
| **pathpy.removedirs_p**\ ``(self)``

| **pathpy.removedirs_p**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.removedirs_p>`__

.. code:: python

        def removedirs_p(self):
            """ Like :meth:`removedirs`, but does not raise an exception if the
            directory is not empty or does not exist. """
            try:
                self.removedirs()
            except OSError:
                _, e, _ = sys.exc_info()
                if e.errno != errno.ENOTEMPTY and e.errno != errno.EEXIST:
                    raise
            return self



``rename``
===========
| **os.rename**\ ``(src, dst, *, src_dir_fd=None, dst_dir_fd=None)``
| **pathlib.rename**\ ``(self, target)``
| **pathpy.rename**\ ``(self, new)``

| **os.rename**\ ``(src, dst, *, src_dir_fd=None, dst_dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.rename>`__

.. code:: python

    Rename a file or directory.

    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.

| **pathlib.rename**\ ``(self, target)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.rename>`__

.. code:: python

        def rename(self, target):
            """
            Rename this path to the given path.
            """
            if self._closed:
                self._raise_closed()
            self._accessor.rename(self, target)


| **pathpy.rename**\ ``(self, new)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rename>`__

.. code:: python

        def rename(self, new):
            """ .. seealso:: :func:`os.rename` """
            os.rename(self, new)
            return self._next_class(new)



``renames``
============
| **os.renames**\ ``(old, new)``
| **pathpy.renames**\ ``(self, new)``

| **os.renames**\ ``(old, new)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.renames>`__

.. code:: python

    def renames(old, new):
        """renames(old, new)

        Super-rename; create directories as necessary and delete any left
        empty.  Works like rename, except creation of any intermediate
        directories needed to make the new pathname good is attempted
        first.  After the rename, directories corresponding to rightmost
        path segments of the old name will be pruned until either the
        whole path is consumed or a nonempty directory is found.

        Note: this function can fail with the new directory structure made
        if you lack permissions needed to unlink the leaf directory or
        file.

        """
        head, tail = path.split(new)
        if head and tail and not path.exists(head):
            makedirs(head)
        rename(old, new)
        head, tail = path.split(old)
        if head and tail:
            try:
                removedirs(head)
            except OSError:
                pass


| **pathpy.renames**\ ``(self, new)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.renames>`__

.. code:: python

        def renames(self, new):
            """ .. seealso:: :func:`os.renames` """
            os.renames(self, new)
            return self._next_class(new)



``replace``
============
| **os.replace**\ ``(src, dst, *, src_dir_fd=None, dst_dir_fd=None)``
| **pathlib.replace**\ ``(self, target)``

| **os.replace**\ ``(src, dst, *, src_dir_fd=None, dst_dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.replace>`__

.. code:: python

    Rename a file or directory, overwriting the destination.

    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError."

| **pathlib.replace**\ ``(self, target)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.replace>`__

.. code:: python

        def replace(self, target):
            """
            Rename this path to the given path, clobbering the existing
            destination if it exists.
            """
            if self._closed:
                self._raise_closed()
            self._accessor.replace(self, target)


| **pathpy.replace**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.replace>`__

.. code:: python

    S.replace(old, new[, count]) -> str

    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.


``resolve``
============
| **pathlib.resolve**\ ``(self, strict=False)``

| **pathlib.resolve**\ ``(self, strict=False)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve>`__

.. code:: python

        def resolve(self, strict=False):
            """
            Make the path absolute, resolving all symlinks on the way and also
            normalizing it (for example turning slashes into backslashes under
            Windows).
            """
            if self._closed:
                self._raise_closed()
            s = self._flavour.resolve(self, strict=strict)
            if s is None:
                # No symlink resolution => for consistency, raise an error if
                # the path doesn't exist or is forbidden
                self.stat()
                s = str(self.absolute())
            # Now we have no symlinks in the path, it's safe to normalize it.
            normed = self._flavour.pathmod.normpath(s)
            obj = self._from_parts((normed,), init=False)
            obj._init(template=self)
            return obj



``rfind``
==========

| **pathpy.rfind**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rfind>`__

.. code:: python

    S.rfind(sub[, start[, end]]) -> int

    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.


``rglob``
==========
| **pathlib.rglob**\ ``(self, pattern)``

| **pathlib.rglob**\ ``(self, pattern)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob>`__

.. code:: python

        def rglob(self, pattern):
            """Recursively yield all existing files (of any kind, including
            directories) matching the given pattern, anywhere in this subtree.
            """
            pattern = self._flavour.casefold(pattern)
            drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
            if drv or root:
                raise NotImplementedError("Non-relative patterns are unsupported")
            selector = _make_selector(("**",) + tuple(pattern_parts))
            for p in selector.select_from(self):
                yield p



``rindex``
===========

| **pathpy.rindex**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rindex>`__

.. code:: python

    S.rindex(sub[, start[, end]]) -> int

    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Raises ValueError when the substring is not found.


``rjust``
==========

| **pathpy.rjust**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rjust>`__

.. code:: python

    S.rjust(width[, fillchar]) -> str

    Return S right-justified in a string of length width. Padding is
    done using the specified fill character (default is a space).


``rmdir``
==========
| **os.rmdir**\ ``(path, *, dir_fd=None)``
| **pathlib.rmdir**\ ``(self)``
| **pathpy.rmdir**\ ``(self)``

| **os.rmdir**\ ``(path, *, dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.rmdir>`__

.. code:: python

    Remove a directory.

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

| **pathlib.rmdir**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.rmdir>`__

.. code:: python

        def rmdir(self):
            """
            Remove this directory.  The directory must be empty.
            """
            if self._closed:
                self._raise_closed()
            self._accessor.rmdir(self)


| **pathpy.rmdir**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rmdir>`__

.. code:: python

        def rmdir(self):
            """ .. seealso:: :func:`os.rmdir` """
            os.rmdir(self)
            return self



``rmdir_p``
============
| **pathpy.rmdir_p**\ ``(self)``

| **pathpy.rmdir_p**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rmdir_p>`__

.. code:: python

        def rmdir_p(self):
            """ Like :meth:`rmdir`, but does not raise an exception if the
            directory is not empty or does not exist. """
            try:
                self.rmdir()
            except OSError:
                _, e, _ = sys.exc_info()
                bypass_codes = errno.ENOTEMPTY, errno.EEXIST, errno.ENOENT
                if e.errno not in bypass_codes:
                    raise
            return self



``rmtree``
===========
| **shutil.rmtree**\ ``(path, ignore_errors=False, onerror=None)``
| **pathpy.rmtree**\ ``(path, ignore_errors=False, onerror=None)``

| **shutil.rmtree**\ ``(path, ignore_errors=False, onerror=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.rmtree>`__

.. code:: python

    def rmtree(path, ignore_errors=False, onerror=None):
        """Recursively delete a directory tree.

        If ignore_errors is set, errors are ignored; otherwise, if onerror
        is set, it is called to handle the error with arguments (func,
        path, exc_info) where func is platform and implementation dependent;
        path is the argument to that function that caused it to fail; and
        exc_info is a tuple returned by sys.exc_info().  If ignore_errors
        is false and onerror is None, an exception is raised.

        """
        if ignore_errors:
            def onerror(*args):
                pass
        elif onerror is None:
            def onerror(*args):
                raise
        if _use_fd_functions:
            # While the unsafe rmtree works fine on bytes, the fd based does not.
            if isinstance(path, bytes):
                path = os.fsdecode(path)
            # Note: To guard against symlink races, we use the standard
            # lstat()/open()/fstat() trick.
            try:
                orig_st = os.lstat(path)
            except Exception:
                onerror(os.lstat, path, sys.exc_info())
                return
            try:
                fd = os.open(path, os.O_RDONLY)
            except Exception:
                onerror(os.lstat, path, sys.exc_info())
                return
            try:
                if os.path.samestat(orig_st, os.fstat(fd)):
                    _rmtree_safe_fd(fd, path, onerror)
                    try:
                        os.rmdir(path)
                    except OSError:
                        onerror(os.rmdir, path, sys.exc_info())
                else:
                    try:
                        # symlinks to directories are forbidden, see bug #1669
                        raise OSError("Cannot call rmtree on a symbolic link")
                    except OSError:
                        onerror(os.path.islink, path, sys.exc_info())
            finally:
                os.close(fd)
        else:
            return _rmtree_unsafe(path, onerror)


| **pathpy.rmtree**\ ``(path, ignore_errors=False, onerror=None)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rmtree>`__

.. code:: python

    def rmtree(path, ignore_errors=False, onerror=None):
        """Recursively delete a directory tree.

        If ignore_errors is set, errors are ignored; otherwise, if onerror
        is set, it is called to handle the error with arguments (func,
        path, exc_info) where func is platform and implementation dependent;
        path is the argument to that function that caused it to fail; and
        exc_info is a tuple returned by sys.exc_info().  If ignore_errors
        is false and onerror is None, an exception is raised.

        """
        if ignore_errors:
            def onerror(*args):
                pass
        elif onerror is None:
            def onerror(*args):
                raise
        if _use_fd_functions:
            # While the unsafe rmtree works fine on bytes, the fd based does not.
            if isinstance(path, bytes):
                path = os.fsdecode(path)
            # Note: To guard against symlink races, we use the standard
            # lstat()/open()/fstat() trick.
            try:
                orig_st = os.lstat(path)
            except Exception:
                onerror(os.lstat, path, sys.exc_info())
                return
            try:
                fd = os.open(path, os.O_RDONLY)
            except Exception:
                onerror(os.lstat, path, sys.exc_info())
                return
            try:
                if os.path.samestat(orig_st, os.fstat(fd)):
                    _rmtree_safe_fd(fd, path, onerror)
                    try:
                        os.rmdir(path)
                    except OSError:
                        onerror(os.rmdir, path, sys.exc_info())
                else:
                    try:
                        # symlinks to directories are forbidden, see bug #1669
                        raise OSError("Cannot call rmtree on a symbolic link")
                    except OSError:
                        onerror(os.path.islink, path, sys.exc_info())
            finally:
                os.close(fd)
        else:
            return _rmtree_unsafe(path, onerror)



``rmtree_p``
=============
| **pathpy.rmtree_p**\ ``(self)``

| **pathpy.rmtree_p**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rmtree_p>`__

.. code:: python

        def rmtree_p(self):
            """ Like :meth:`rmtree`, but does not raise an exception if the
            directory does not exist. """
            try:
                self.rmtree()
            except OSError:
                _, e, _ = sys.exc_info()
                if e.errno != errno.ENOENT:
                    raise
            return self



``root``
=========

| **pathlib.root**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.root>`__

.. code:: python

    The root of the path, if any.


``rpartition``
===============

| **pathpy.rpartition**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rpartition>`__

.. code:: python

    S.rpartition(sep) -> (head, sep, tail)

    Search for the separator sep in S, starting at the end of S, and return
    the part before it, the separator itself, and the part after it.  If the
    separator is not found, return two empty strings and S.


``rsplit``
===========

| **pathpy.rsplit**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rsplit>`__

.. code:: python

    S.rsplit(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string, starting at the end of the string and
    working to the front.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified, any whitespace string
    is a separator.


``rstrip``
===========

| **pathpy.rstrip**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.rstrip>`__

.. code:: python

    S.rstrip([chars]) -> str

    Return a copy of the string S with trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead.


``samefile``
=============
| **os.path.samefile**\ ``(f1, f2)``
| **pathlib.samefile**\ ``(self, other_path)``
| **pathpy.samefile**\ ``(self, other)``

| **os.path.samefile**\ ``(f1, f2)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.samefile>`__

.. code:: python

    def samefile(f1, f2):
        """Test whether two pathnames reference the same actual file"""
        s1 = os.stat(f1)
        s2 = os.stat(f2)
        return samestat(s1, s2)


| **pathlib.samefile**\ ``(self, other_path)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.samefile>`__

.. code:: python

        def samefile(self, other_path):
            """Return whether other_path is the same or not as this file
            (as returned by os.path.samefile()).
            """
            st = self.stat()
            try:
                other_st = other_path.stat()
            except AttributeError:
                other_st = os.stat(other_path)
            return os.path.samestat(st, other_st)


| **pathpy.samefile**\ ``(self, other)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.samefile>`__

.. code:: python

        def samefile(self, other):
            """ .. seealso:: :func:`os.path.samefile` """
            if not hasattr(self.module, 'samefile'):
                other = Path(other).realpath().normpath().normcase()
                return self.realpath().normpath().normcase() == other
            return self.module.samefile(self, other)



``sameopenfile``
=================
| **os.path.sameopenfile**\ ``(fp1, fp2)``

| **os.path.sameopenfile**\ ``(fp1, fp2)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.sameopenfile>`__

.. code:: python

    def sameopenfile(fp1, fp2):
        """Test whether two open file objects reference the same file"""
        s1 = os.fstat(fp1)
        s2 = os.fstat(fp2)
        return samestat(s1, s2)



``samestat``
=============
| **os.path.samestat**\ ``(s1, s2)``

| **os.path.samestat**\ ``(s1, s2)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.samestat>`__

.. code:: python

    def samestat(s1, s2):
        """Test whether two stat buffers reference the same file"""
        return (s1.st_ino == s2.st_ino and
                s1.st_dev == s2.st_dev)



``sep``
========

| **os.sep**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.sep>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

| **os.path.sep**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.sep>`__

.. code:: python

    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.


``size``
=========

| seealso: `pathpy.getsize <#getsize>`_
 
| **pathpy.size**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.size>`__

.. code:: python

    Size of the file, in bytes.

    .. seealso:: :meth:`getsize`, :func:`os.path.getsize`


``special``
============
| **pathpy.special**\ ``(*args, **kwargs)``

| **pathpy.special**\ ``(*args, **kwargs)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.special>`__

.. code:: python

    partial(func, *args, **keywords) - new function with partial application
    of the given arguments and keywords.


``split``
==========
| **os.path.split**\ ``(p)``

| **os.path.split**\ ``(p)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.split>`__

.. code:: python

    def split(p):
        """Split a pathname.  Returns tuple "(head, tail)" where "tail" is
        everything after the final slash.  Either part may be empty."""
        p = os.fspath(p)
        sep = _get_sep(p)
        i = p.rfind(sep) + 1
        head, tail = p[:i], p[i:]
        if head and head != sep*len(head):
            head = head.rstrip(sep)
        return head, tail


| **pathpy.split**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.split>`__

.. code:: python

    S.split(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.


``splitall``
=============
| **pathpy.splitall**\ ``(self)``

| **pathpy.splitall**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.splitall>`__

.. code:: python

        def splitall(self):
            r""" Return a list of the path components in this path.

            The first item in the list will be a Path.  Its value will be
            either :data:`os.curdir`, :data:`os.pardir`, empty, or the root
            directory of this path (for example, ``'/'`` or ``'C:\\'``).  The
            other items in the list will be strings.

            ``path.Path.joinpath(*result)`` will yield the original path.
            """
            parts = []
            loc = self
            while loc != os.curdir and loc != os.pardir:
                prev = loc
                loc, child = prev.splitpath()
                if loc == prev:
                    break
                parts.append(child)
            parts.append(loc)
            parts.reverse()
            return parts



``splitdrive``
===============
| **os.path.splitdrive**\ ``(p)``
| **pathpy.splitdrive**\ ``(self)``

| **os.path.splitdrive**\ ``(p)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.splitdrive>`__

.. code:: python

    def splitdrive(p):
        """Split a pathname into drive and path. On Posix, drive is always
        empty."""
        p = os.fspath(p)
        return p[:0], p


| **pathpy.splitdrive**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.splitdrive>`__

.. code:: python

        def splitdrive(self):
            """ p.splitdrive() -> Return ``(p.drive, <the rest of p>)``.

            Split the drive specifier from this path.  If there is
            no drive specifier, :samp:`{p.drive}` is empty, so the return value
            is simply ``(Path(''), p)``.  This is always the case on Unix.

            .. seealso:: :func:`os.path.splitdrive`
            """
            drive, rel = self.module.splitdrive(self)
            return self._next_class(drive), rel



``splitext``
=============
| **os.path.splitext**\ ``(p)``
| **pathpy.splitext**\ ``(self)``

| **os.path.splitext**\ ``(p)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.splitext>`__

.. code:: python

    def splitext(p):
        p = os.fspath(p)
        if isinstance(p, bytes):
            sep = b'/'
            extsep = b'.'
        else:
            sep = '/'
            extsep = '.'
        return genericpath._splitext(p, sep, None, extsep)


| **pathpy.splitext**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.splitext>`__

.. code:: python

        def splitext(self):
            """ p.splitext() -> Return ``(p.stripext(), p.ext)``.

            Split the filename extension from this path and return
            the two parts.  Either part may be empty.

            The extension is everything from ``'.'`` to the end of the
            last path segment.  This has the property that if
            ``(a, b) == p.splitext()``, then ``a + b == p``.

            .. seealso:: :func:`os.path.splitext`
            """
            filename, ext = self.module.splitext(self)
            return self._next_class(filename), ext



``splitlines``
===============

| **pathpy.splitlines**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.splitlines>`__

.. code:: python

    S.splitlines([keepends]) -> list of strings

    Return a list of the lines in S, breaking at line boundaries.
    Line breaks are not included in the resulting list unless keepends
    is given and true.


``splitpath``
==============
| **pathpy.splitpath**\ ``(self)``

| **pathpy.splitpath**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.splitpath>`__

.. code:: python

        def splitpath(self):
            """ p.splitpath() -> Return ``(p.parent, p.name)``.

            .. seealso:: :attr:`parent`, :attr:`name`, :func:`os.path.split`
            """
            parent, child = self.module.split(self)
            return self._next_class(parent), child



``splitunc``
=============
| **pathpy.splitunc**\ ``(self)``

| **pathpy.splitunc**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.splitunc>`__

.. code:: python

        def splitunc(self):
            """ .. seealso:: :func:`os.path.splitunc` """
            unc, rest = self.module.splitunc(self)
            return self._next_class(unc), rest



``startswith``
===============

| **pathpy.startswith**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.startswith>`__

.. code:: python

    S.startswith(prefix[, start[, end]]) -> bool

    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.


``stat``
=========
| **os.stat**\ ``(path, *, dir_fd=None, follow_symlinks=True)``
| **pathlib.stat**\ ``(self)``
| **pathpy.stat**\ ``(self)``

| **os.stat**\ ``(path, *, dir_fd=None, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.stat>`__

.. code:: python

    Perform a stat system call on the given path.

      path
        Path to be examined; can be string, bytes, path-like object or
        open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be a relative string; path will then be relative to
        that directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.

    dir_fd and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.

    It's an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.

| **os.path.stat**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/posixpath.py>`__ `docs <https://docs.python.org/3/library/os.path.html#os.path.stat>`__

.. code:: python

    Constants/functions for interpreting results of os.stat() and os.lstat().

    Suggested usage: from stat import *

| **shutil.stat**:
| `source <https://github.com/python/cpython/tree/3.6/Lib/shutil.py>`__ `docs <https://docs.python.org/3/library/shutil.html#shutil.stat>`__

.. code:: python

    Constants/functions for interpreting results of os.stat() and os.lstat().

    Suggested usage: from stat import *

| **pathlib.stat**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat>`__

.. code:: python

        def stat(self):
            """
            Return the result of the stat() system call on this path, like
            os.stat() does.
            """
            return self._accessor.stat(self)


| **pathpy.stat**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.stat>`__

.. code:: python

        def stat(self):
            """ Perform a ``stat()`` system call on this path.

            .. seealso:: :meth:`lstat`, :func:`os.stat`
            """
            return os.stat(self)



``statvfs``
============
| **os.statvfs**\ ``(path)``
| **pathpy.statvfs**\ ``(self)``

| **os.statvfs**\ ``(path)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.statvfs>`__

.. code:: python

    Perform a statvfs system call on the given path.

    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.

| **pathpy.statvfs**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.statvfs>`__

.. code:: python

            def statvfs(self):
                """ Perform a ``statvfs()`` system call on this path.

                .. seealso:: :func:`os.statvfs`
                """
                return os.statvfs(self)



``stem``
=========

| **pathlib.stem**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.stem>`__

.. code:: python

    The final path component, minus its last suffix.

| **pathpy.stem**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.stem>`__

.. code:: python

    The same as :meth:`name`, but with one file extension stripped off.

    >>> Path('/home/guido/python.tar.gz').stem
    'python.tar'


``strip``
==========

| **pathpy.strip**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.strip>`__

.. code:: python

    S.strip([chars]) -> str

    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.


``stripext``
=============
| **pathpy.stripext**\ ``(self)``

| **pathpy.stripext**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.stripext>`__

.. code:: python

        def stripext(self):
            """ p.stripext() -> Remove one file extension from the path.

            For example, ``Path('/home/guido/python.tar.gz').stripext()``
            returns ``Path('/home/guido/python.tar')``.
            """
            return self.splitext()[0]



``suffix``
===========

| **pathlib.suffix**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.suffix>`__

.. code:: python

    The final component's last suffix, if any.


``suffixes``
=============

| **pathlib.suffixes**:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.suffixes>`__

.. code:: python

    A list of the final component's suffixes, if any.


``swapcase``
=============

| **pathpy.swapcase**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.swapcase>`__

.. code:: python

    S.swapcase() -> str

    Return a copy of S with uppercase characters converted to lowercase
    and vice versa.


``symlink``
============
| **os.symlink**\ ``(src, dst, target_is_directory=False, *, dir_fd=None)``
| **pathpy.symlink**\ ``(self, newlink=None)``

| **os.symlink**\ ``(src, dst, target_is_directory=False, *, dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.symlink>`__

.. code:: python

    Create a symbolic link pointing to src named dst.

    target_is_directory is required on Windows if the target is to be
      interpreted as a directory.  (On Windows, symlink requires
      Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
      target_is_directory is ignored on non-Windows platforms.

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

| **pathpy.symlink**\ ``(self, newlink=None)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.symlink>`__

.. code:: python

            def symlink(self, newlink=None):
                """ Create a symbolic link at `newlink`, pointing here.

                If newlink is not supplied, the symbolic link will assume
                the name self.basename(), creating the link in the cwd.

                .. seealso:: :func:`os.symlink`
                """
                if newlink is None:
                    newlink = self.basename()
                os.symlink(self, newlink)
                return self._next_class(newlink)



``symlink_to``
===============
| **pathlib.symlink_to**\ ``(self, target, target_is_directory=False)``

| **pathlib.symlink_to**\ ``(self, target, target_is_directory=False)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.symlink_to>`__

.. code:: python

        def symlink_to(self, target, target_is_directory=False):
            """
            Make this path a symlink pointing to the given path.
            Note the order of arguments (self, target) is the reverse of os.symlink's.
            """
            if self._closed:
                self._raise_closed()
            self._accessor.symlink(target, self, target_is_directory)



``text``
=========
| **pathpy.text**\ ``(self, encoding=None, errors='strict')``

| **pathpy.text**\ ``(self, encoding=None, errors='strict')``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.text>`__

.. code:: python

        def text(self, encoding=None, errors='strict'):
            r""" Open this file, read it in, return the content as a string.

            All newline sequences are converted to ``'\n'``.  Keyword arguments
            will be passed to :meth:`open`.

            .. seealso:: :meth:`lines`
            """
            with self.open(mode='r', encoding=encoding, errors=errors) as f:
                return U_NEWLINE.sub('\n', f.read())



``title``
==========

| **pathpy.title**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.title>`__

.. code:: python

    S.title() -> str

    Return a titlecased version of S, i.e. words start with title case
    characters, all remaining cased characters have lower case.


``touch``
==========
| **pathlib.touch**\ ``(self, mode=438, exist_ok=True)``
| **pathpy.touch**\ ``(self)``

| **pathlib.touch**\ ``(self, mode=438, exist_ok=True)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.touch>`__

.. code:: python

        def touch(self, mode=0o666, exist_ok=True):
            """
            Create this file with the given access mode, if it doesn't exist.
            """
            if self._closed:
                self._raise_closed()
            if exist_ok:
                # First try to bump modification time
                # Implementation note: GNU touch uses the UTIME_NOW option of
                # the utimensat() / futimens() functions.
                try:
                    self._accessor.utime(self, None)
                except OSError:
                    # Avoid exception chaining
                    pass
                else:
                    return
            flags = os.O_CREAT | os.O_WRONLY
            if not exist_ok:
                flags |= os.O_EXCL
            fd = self._raw_open(flags, mode)
            os.close(fd)


| **pathpy.touch**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.touch>`__

.. code:: python

        def touch(self):
            """ Set the access/modified times of this file to the current time.
            Create the file if it does not exist.
            """
            fd = os.open(self, os.O_WRONLY | os.O_CREAT, 0o666)
            os.close(fd)
            os.utime(self, None)
            return self



``translate``
==============

| **pathpy.translate**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.translate>`__

.. code:: python

    S.translate(table) -> str

    Return a copy of the string S in which each character has been mapped
    through the given translation table. The table must implement
    lookup/indexing via __getitem__, for instance a dictionary or list,
    mapping Unicode ordinals to Unicode ordinals, strings, or None. If
    this operation raises LookupError, the character is left untouched.
    Characters mapped to None are deleted.


``uncshare``
=============

| **pathpy.uncshare**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.uncshare>`__

.. code:: python

    The UNC mount point for this path.
    This is empty for paths on local drives.


``unlink``
===========
| **os.unlink**\ ``(path, *, dir_fd=None)``
| **pathlib.unlink**\ ``(self)``
| **pathpy.unlink**\ ``(self)``

| **os.unlink**\ ``(path, *, dir_fd=None)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.unlink>`__

.. code:: python

    Remove a file (same as remove()).

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

| **pathlib.unlink**\ ``(self)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink>`__

.. code:: python

        def unlink(self):
            """
            Remove this file or link.
            If the path is a directory, use rmdir() instead.
            """
            if self._closed:
                self._raise_closed()
            self._accessor.unlink(self)


| **pathpy.unlink**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.unlink>`__

.. code:: python

        def unlink(self):
            """ .. seealso:: :func:`os.unlink` """
            os.unlink(self)
            return self



``unlink_p``
=============
| **pathpy.unlink_p**\ ``(self)``

| **pathpy.unlink_p**\ ``(self)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.unlink_p>`__

.. code:: python

        def unlink_p(self):
            """ Like :meth:`unlink`, but does not raise an exception if the
            file does not exist. """
            self.remove_p()
            return self



``upper``
==========

| **pathpy.upper**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.upper>`__

.. code:: python

    S.upper() -> str

    Return a copy of S converted to uppercase.


``using_module``
=================
| **pathpy.using_module**\ ``(module)``

| **pathpy.using_module**\ ``(module)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.using_module>`__

.. code:: python

        def wrapper(cls, module):
            if module in saved_results:
                return saved_results[module]
            saved_results[module] = func(cls, module)
            return saved_results[module]



``utime``
==========
| **os.utime**\ ``(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True)``
| **pathpy.utime**\ ``(self, times)``

| **os.utime**\ ``(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.utime>`__

.. code:: python

    Set the access and modified time of path.

    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.

    If times is not None, it must be a tuple (atime, mtime);
        atime and mtime should be expressed as float seconds since the epoch.
    If ns is specified, it must be a tuple (atime_ns, mtime_ns);
        atime_ns and mtime_ns should be expressed as integer nanoseconds
        since the epoch.
    If times is None and ns is unspecified, utime uses the current time.
    Specifying tuples for both times and ns is an error.

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, utime will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path
      as an open file descriptor.
    dir_fd and follow_symlinks may not be available on your platform.
      If they are unavailable, using them will raise a NotImplementedError.

| **pathpy.utime**\ ``(self, times)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.utime>`__

.. code:: python

        def utime(self, times):
            """ Set the access and modified times of this file.

            .. seealso:: :func:`os.utime`
            """
            os.utime(self, times)
            return self



``walk``
=========
| **os.walk**\ ``(top, topdown=True, onerror=None, followlinks=False)``
| **pathpy.walk**\ ``(self, pattern=None, errors='strict')``

| **os.walk**\ ``(top, topdown=True, onerror=None, followlinks=False)``:
| `source <https://github.com/python/cpython/tree/3.6/Lib/os.py>`__ `docs <https://docs.python.org/3/library/os.html#os.walk>`__

.. code:: python

    def walk(top, topdown=True, onerror=None, followlinks=False):
        """Directory tree generator.

        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple

            dirpath, dirnames, filenames

        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).

        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).

        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune the
        search, or to impose a specific order of visiting.  Modifying dirnames when
        topdown is false is ineffective, since the directories in dirnames have
        already been generated by the time dirnames itself is generated. No matter
        the value of topdown, the list of subdirectories is retrieved before the
        tuples for the directory and its subdirectories are generated.

        By default errors from the os.scandir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an OSError instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.

        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.

        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.

        Example:

        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum([getsize(join(root, name)) for name in files]), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories

        """
        top = fspath(top)
        dirs = []
        nondirs = []
        walk_dirs = []

        # We may not have read permission for top, in which case we can't
        # get a list of the files the directory contains.  os.walk
        # always suppressed the exception then, rather than blow up for a
        # minor reason when (say) a thousand readable directories are still
        # left to visit.  That logic is copied here.
        try:
            # Note that scandir is global in this module due
            # to earlier import-*.
            scandir_it = scandir(top)
        except OSError as error:
            if onerror is not None:
                onerror(error)
            return

        with scandir_it:
            while True:
                try:
                    try:
                        entry = next(scandir_it)
                    except StopIteration:
                        break
                except OSError as error:
                    if onerror is not None:
                        onerror(error)
                    return

                try:
                    is_dir = entry.is_dir()
                except OSError:
                    # If is_dir() raises an OSError, consider that the entry is not
                    # a directory, same behaviour than os.path.isdir().
                    is_dir = False

                if is_dir:
                    dirs.append(entry.name)
                else:
                    nondirs.append(entry.name)

                if not topdown and is_dir:
                    # Bottom-up: recurse into sub-directory, but exclude symlinks to
                    # directories if followlinks is False
                    if followlinks:
                        walk_into = True
                    else:
                        try:
                            is_symlink = entry.is_symlink()
                        except OSError:
                            # If is_symlink() raises an OSError, consider that the
                            # entry is not a symbolic link, same behaviour than
                            # os.path.islink().
                            is_symlink = False
                        walk_into = not is_symlink

                    if walk_into:
                        walk_dirs.append(entry.path)

        # Yield before recursion if going top down
        if topdown:
            yield top, dirs, nondirs

            # Recurse into sub-directories
            islink, join = path.islink, path.join
            for dirname in dirs:
                new_path = join(top, dirname)
                # Issue #23605: os.path.islink() is used instead of caching
                # entry.is_symlink() result during the loop on os.scandir() because
                # the caller can replace the directory entry during the "yield"
                # above.
                if followlinks or not islink(new_path):
                    yield from walk(new_path, topdown, onerror, followlinks)
        else:
            # Recurse into sub-directories
            for new_path in walk_dirs:
                yield from walk(new_path, topdown, onerror, followlinks)
            # Yield after recursion if going bottom up
            yield top, dirs, nondirs


| **pathpy.walk**\ ``(self, pattern=None, errors='strict')``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.walk>`__

.. code:: python

        def walk(self, pattern=None, errors='strict'):
            """ D.walk() -> iterator over files and subdirs, recursively.

            The iterator yields Path objects naming each child item of
            this directory and its descendants.  This requires that
            ``D.isdir()``.

            This performs a depth-first traversal of the directory tree.
            Each directory is returned just before all its children.

            The `errors=` keyword argument controls behavior when an
            error occurs.  The default is ``'strict'``, which causes an
            exception.  Other allowed values are ``'warn'`` (which
            reports the error via :func:`warnings.warn()`), and ``'ignore'``.
            `errors` may also be an arbitrary callable taking a msg parameter.
            """
            class Handlers:
                def strict(msg):
                    raise

                def warn(msg):
                    warnings.warn(msg, TreeWalkWarning)

                def ignore(msg):
                    pass

            if not callable(errors) and errors not in vars(Handlers):
                raise ValueError("invalid errors parameter")
            errors = vars(Handlers).get(errors, errors)

            try:
                childList = self.listdir()
            except Exception:
                exc = sys.exc_info()[1]
                tmpl = "Unable to list directory '%(self)s': %(exc)s"
                msg = tmpl % locals()
                errors(msg)
                return

            for child in childList:
                if pattern is None or child.fnmatch(pattern):
                    yield child
                try:
                    isdir = child.isdir()
                except Exception:
                    exc = sys.exc_info()[1]
                    tmpl = "Unable to access '%(child)s': %(exc)s"
                    msg = tmpl % locals()
                    errors(msg)
                    isdir = False

                if isdir:
                    for item in child.walk(pattern, errors):
                        yield item



``walkdirs``
=============
| **pathpy.walkdirs**\ ``(self, pattern=None, errors='strict')``

| **pathpy.walkdirs**\ ``(self, pattern=None, errors='strict')``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.walkdirs>`__

.. code:: python

        def walkdirs(self, pattern=None, errors='strict'):
            """ D.walkdirs() -> iterator over subdirs, recursively.

            With the optional `pattern` argument, this yields only
            directories whose names match the given pattern.  For
            example, ``mydir.walkdirs('*test')`` yields only directories
            with names ending in ``'test'``.

            The `errors=` keyword argument controls behavior when an
            error occurs.  The default is ``'strict'``, which causes an
            exception.  The other allowed values are ``'warn'`` (which
            reports the error via :func:`warnings.warn()`), and ``'ignore'``.
            """
            if errors not in ('strict', 'warn', 'ignore'):
                raise ValueError("invalid errors parameter")

            try:
                dirs = self.dirs()
            except Exception:
                if errors == 'ignore':
                    return
                elif errors == 'warn':
                    warnings.warn(
                        "Unable to list directory '%s': %s"
                        % (self, sys.exc_info()[1]),
                        TreeWalkWarning)
                    return
                else:
                    raise

            for child in dirs:
                if pattern is None or child.fnmatch(pattern):
                    yield child
                for subsubdir in child.walkdirs(pattern, errors):
                    yield subsubdir



``walkfiles``
==============
| **pathpy.walkfiles**\ ``(self, pattern=None, errors='strict')``

| **pathpy.walkfiles**\ ``(self, pattern=None, errors='strict')``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.walkfiles>`__

.. code:: python

        def walkfiles(self, pattern=None, errors='strict'):
            """ D.walkfiles() -> iterator over files in D, recursively.

            The optional argument `pattern` limits the results to files
            with names that match the pattern.  For example,
            ``mydir.walkfiles('*.tmp')`` yields only files with the ``.tmp``
            extension.
            """
            if errors not in ('strict', 'warn', 'ignore'):
                raise ValueError("invalid errors parameter")

            try:
                childList = self.listdir()
            except Exception:
                if errors == 'ignore':
                    return
                elif errors == 'warn':
                    warnings.warn(
                        "Unable to list directory '%s': %s"
                        % (self, sys.exc_info()[1]),
                        TreeWalkWarning)
                    return
                else:
                    raise

            for child in childList:
                try:
                    isfile = child.isfile()
                    isdir = not isfile and child.isdir()
                except Exception:
                    if errors == 'ignore':
                        continue
                    elif errors == 'warn':
                        warnings.warn(
                            "Unable to access '%s': %s"
                            % (self, sys.exc_info()[1]),
                            TreeWalkWarning)
                        continue
                    else:
                        raise

                if isfile:
                    if pattern is None or child.fnmatch(pattern):
                        yield child
                elif isdir:
                    for f in child.walkfiles(pattern, errors):
                        yield f



``with_name``
==============
| **pathlib.with_name**\ ``(self, name)``

| **pathlib.with_name**\ ``(self, name)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.with_name>`__

.. code:: python

        def with_name(self, name):
            """Return a new path with the file name changed."""
            if not self.name:
                raise ValueError("%r has an empty name" % (self,))
            drv, root, parts = self._flavour.parse_parts((name,))
            if (not name or name[-1] in [self._flavour.sep, self._flavour.altsep]
                or drv or root or len(parts) != 1):
                raise ValueError("Invalid name %r" % (name))
            return self._from_parsed_parts(self._drv, self._root,
                                           self._parts[:-1] + [name])



``with_suffix``
================
| **pathlib.with_suffix**\ ``(self, suffix)``
| **pathpy.with_suffix**\ ``(self, suffix)``

| **pathlib.with_suffix**\ ``(self, suffix)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.with_suffix>`__

.. code:: python

        def with_suffix(self, suffix):
            """Return a new path with the file suffix changed (or added, if none)."""
            # XXX if suffix is None, should the current suffix be removed?
            f = self._flavour
            if f.sep in suffix or f.altsep and f.altsep in suffix:
                raise ValueError("Invalid suffix %r" % (suffix))
            if suffix and not suffix.startswith('.') or suffix == '.':
                raise ValueError("Invalid suffix %r" % (suffix))
            name = self.name
            if not name:
                raise ValueError("%r has an empty name" % (self,))
            old_suffix = self.suffix
            if not old_suffix:
                name = name + suffix
            else:
                name = name[:-len(old_suffix)] + suffix
            return self._from_parsed_parts(self._drv, self._root,
                                           self._parts[:-1] + [name])


| **pathpy.with_suffix**\ ``(self, suffix)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.with_suffix>`__

.. code:: python

        def with_suffix(self, suffix):
            """ Return a new path with the file suffix changed (or added, if none)

            >>> Path('/home/guido/python.tar.gz').with_suffix(".foo")
            Path('/home/guido/python.tar.foo')

            >>> Path('python').with_suffix('.zip')
            Path('python.zip')

            >>> Path('filename.ext').with_suffix('zip')
            Traceback (most recent call last):
            ...
            ValueError: Invalid suffix 'zip'
            """
            if not suffix.startswith('.'):
                raise ValueError("Invalid suffix {suffix!r}".format(**locals()))

            return self.stripext() + suffix



``write_bytes``
================
| **pathlib.write_bytes**\ ``(self, data)``
| **pathpy.write_bytes**\ ``(self, bytes, append=False)``

| **pathlib.write_bytes**\ ``(self, data)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_bytes>`__

.. code:: python

        def write_bytes(self, data):
            """
            Open the file in bytes mode, write to it, and close the file.
            """
            # type-check for the buffer interface before truncating the file
            view = memoryview(data)
            with self.open(mode='wb') as f:
                return f.write(view)


| **pathpy.write_bytes**\ ``(self, bytes, append=False)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.write_bytes>`__

.. code:: python

        def write_bytes(self, bytes, append=False):
            """ Open this file and write the given bytes to it.

            Default behavior is to overwrite any existing file.
            Call ``p.write_bytes(bytes, append=True)`` to append instead.
            """
            if append:
                mode = 'ab'
            else:
                mode = 'wb'
            with self.open(mode) as f:
                f.write(bytes)



``write_lines``
================
| **pathpy.write_lines**\ ``(self, lines, encoding=None, errors='strict', linesep='\n', append=False)``

| **pathpy.write_lines**\ ``(self, lines, encoding=None, errors='strict', linesep='\n', append=False)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.write_lines>`__

.. code:: python

        def write_lines(self, lines, encoding=None, errors='strict',
                        linesep=os.linesep, append=False):
            r""" Write the given lines of text to this file.

            By default this overwrites any existing file at this path.

            This puts a platform-specific newline sequence on every line.
            See `linesep` below.

                `lines` - A list of strings.

                `encoding` - A Unicode encoding to use.  This applies only if
                    `lines` contains any Unicode strings.

                `errors` - How to handle errors in Unicode encoding.  This
                    also applies only to Unicode strings.

                linesep - The desired line-ending.  This line-ending is
                    applied to every line.  If a line already has any
                    standard line ending (``'\r'``, ``'\n'``, ``'\r\n'``,
                    ``u'\x85'``, ``u'\r\x85'``, ``u'\u2028'``), that will
                    be stripped off and this will be used instead.  The
                    default is os.linesep, which is platform-dependent
                    (``'\r\n'`` on Windows, ``'\n'`` on Unix, etc.).
                    Specify ``None`` to write the lines as-is, like
                    :meth:`file.writelines`.

            Use the keyword argument ``append=True`` to append lines to the
            file.  The default is to overwrite the file.

            .. warning ::

                When you use this with Unicode data, if the encoding of the
                existing data in the file is different from the encoding
                you specify with the `encoding=` parameter, the result is
                mixed-encoding data, which can really confuse someone trying
                to read the file later.
            """
            with self.open('ab' if append else 'wb') as f:
                for line in lines:
                    isUnicode = isinstance(line, text_type)
                    if linesep is not None:
                        pattern = U_NL_END if isUnicode else NL_END
                        line = pattern.sub('', line) + linesep
                    if isUnicode:
                        line = line.encode(
                            encoding or sys.getdefaultencoding(), errors)
                    f.write(line)



``write_text``
===============
| **pathlib.write_text**\ ``(self, data, encoding=None, errors=None)``
| **pathpy.write_text**\ ``(self, text, encoding=None, errors='strict', linesep='\n', append=False)``

| **pathlib.write_text**\ ``(self, data, encoding=None, errors=None)``:
| `source <https://github.com/python/cpython/blob/3.6/Lib/pathlib.py>`__ `docs <https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text>`__

.. code:: python

        def write_text(self, data, encoding=None, errors=None):
            """
            Open the file in text mode, write to it, and close the file.
            """
            if not isinstance(data, str):
                raise TypeError('data must be str, not %s' %
                                data.__class__.__name__)
            with self.open(mode='w', encoding=encoding, errors=errors) as f:
                return f.write(data)


| **pathpy.write_text**\ ``(self, text, encoding=None, errors='strict', linesep='\n', append=False)``:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.write_text>`__

.. code:: python

        def write_text(self, text, encoding=None, errors='strict',
                       linesep=os.linesep, append=False):
            r""" Write the given text to this file.

            The default behavior is to overwrite any existing file;
            to append instead, use the `append=True` keyword argument.

            There are two differences between :meth:`write_text` and
            :meth:`write_bytes`: newline handling and Unicode handling.
            See below.

            Parameters:

              `text` - str/unicode - The text to be written.

              `encoding` - str - The Unicode encoding that will be used.
                  This is ignored if `text` isn't a Unicode string.

              `errors` - str - How to handle Unicode encoding errors.
                  Default is ``'strict'``.  See ``help(unicode.encode)`` for the
                  options.  This is ignored if `text` isn't a Unicode
                  string.

              `linesep` - keyword argument - str/unicode - The sequence of
                  characters to be used to mark end-of-line.  The default is
                  :data:`os.linesep`.  You can also specify ``None`` to
                  leave all newlines as they are in `text`.

              `append` - keyword argument - bool - Specifies what to do if
                  the file already exists (``True``: append to the end of it;
                  ``False``: overwrite it.)  The default is ``False``.


            --- Newline handling.

            ``write_text()`` converts all standard end-of-line sequences
            (``'\n'``, ``'\r'``, and ``'\r\n'``) to your platform's default
            end-of-line sequence (see :data:`os.linesep`; on Windows, for example,
            the end-of-line marker is ``'\r\n'``).

            If you don't like your platform's default, you can override it
            using the `linesep=` keyword argument.  If you specifically want
            ``write_text()`` to preserve the newlines as-is, use ``linesep=None``.

            This applies to Unicode text the same as to 8-bit text, except
            there are three additional standard Unicode end-of-line sequences:
            ``u'\x85'``, ``u'\r\x85'``, and ``u'\u2028'``.

            (This is slightly different from when you open a file for
            writing with ``fopen(filename, "w")`` in C or ``open(filename, 'w')``
            in Python.)


            --- Unicode

            If `text` isn't Unicode, then apart from newline handling, the
            bytes are written verbatim to the file.  The `encoding` and
            `errors` arguments are not used and must be omitted.

            If `text` is Unicode, it is first converted to :func:`bytes` using the
            specified `encoding` (or the default encoding if `encoding`
            isn't specified).  The `errors` argument applies only to this
            conversion.

            """
            if isinstance(text, text_type):
                if linesep is not None:
                    text = U_NEWLINE.sub(linesep, text)
                text = text.encode(encoding or sys.getdefaultencoding(), errors)
            else:
                assert encoding is None
                text = NEWLINE.sub(linesep, text)
            self.write_bytes(text, append=append)



``zfill``
==========

| **pathpy.zfill**:
| `source <https://github.com/jaraco/path.py/blob/master/path.py>`__ `docs <https://pathpy.readthedocs.io/en/latest/api.html#path.Path.zfill>`__

.. code:: python

    S.zfill(width) -> str

    Pad a numeric string S with zeros on the left, to fill a field
    of the specified width. The string S is never truncated.


