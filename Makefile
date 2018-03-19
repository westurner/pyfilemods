
default: build

build:
	python3 pyfilemods/pyfilemods.py > README.rst
	rst2html.py ./README.rst \
		--no-file-insertion \
		--no-raw \
		--link-stylesheet \
		--stylesheet-dirs=_static/ \
		--stylesheet-path=_static/pydoctheme.css,_static/pygments.css,_static/pygments_extra.css \
		--syntax-highlight=short \
		--title="Python File Methods and Attributes" \
		> index.html

CSS = pydoctheme.css pygments.css default.css classic.css basic.css
buildstatic:
	mkdir -p _static/ || true
	curl https://raw.githubusercontent.com/python/python-docs-theme/master/LICENSE -o _static/LICENSE.python-docs-theme
	$(foreach var,$(CSS),curl -Lq https://docs.python.org/3/_static/$(var) -o _static/$(var);)

modifypygmentscss:
	sed -i 's/^.highlight /.python /' _static/pygments.css

createpygmentsextracss:
	echo 'tt, code, pre { font-size: 85% }' > _static/pygments_extra.css

getlicense:
	curl https://raw.githubusercontent.com/python/cpython/master/LICENSE -o LICENSE.cpython
	curl https://raw.githubusercontent.com/jaraco/path.py/master/LICENSE -o LICENSE.pathpy

open:
	python -m webbrowser ./index.html
