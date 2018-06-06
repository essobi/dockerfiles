# DO NOT EDIT, This Dockerfile is generated from
./tools/70_generate_Dockerfile.sh  
FROM bjodah/bjodahimg16base:v1.2  
MAINTAINER Björn Dahlgren <bjodah@DELETEMEgmail.com>  
RUN \  
apt-get update && apt-get --quiet --assume-yes --no-install-recommends install
texlive-generic-recommended texlive-latex-recommended texlive-science texlive-
fonts-recommended \  
texlive-fonts-extra texlive-latex-extra texlive-lang-european lmodern texlive-
bibtex-extra texlive-math-extra biber \  
graphviz dot2tex dvipng latexmk sudo \  
freeglut3-dev libglfw3-dev \  
expect xutils-dev cmake \  
libfontconfig1 imagemagick \  
python-rdkit librdkit1 rdkit-data \  
libxrender1 fonts-dejavu pandoc \  
libgsl-dev libsundials-serial-dev coinor-libipopt-dev \  
libboost-all-dev libboost1.58-tools-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN \  
cd /tmp && \  
for FNAME in alabaster-0.7.10-py2.py3-none-any.whl apipkg-1.4-py2.py3-none-
any.whl argh-0.26.2-py2.py3-none-any.whl ase-3.14.1-py2-none-any.whl
ase-3.14.1.tar.gz Babel-2.5.0-py2.py3-none-any.whl
backports_abc-0.5-py2.py3-none-any.whl
backports.shutil_get_terminal_size-1.0.0-py2.py3-none-any.whl
bkcharts-0.2.tar.gz bleach-2.0.0-py2.py3-none-any.whl blinker-1.4.tar.gz
bokeh-0.12.6.tar.gz bottle-0.12.13.tar.gz cclib-1.4.1.tar.gz
certifi-2017.7.27.1-py2.py3-none-any.whl chardet-3.0.4-py2.py3-none-any.whl
cheroot-5.8.3-py2.py3-none-any.whl CherryPy-11.0.0-py2.py3-none-any.whl
click-6.7-py2.py3-none-any.whl cloudpickle-0.4.0-py2.py3-none-any.whl
configparser-3.5.0.tar.gz coverage-4.4.1-cp27-cp27mu-manylinux1_x86_64.whl
coverage-4.4.1-cp35-cp35m-manylinux1_x86_64.whl cycler-0.10.0-py2.py3-none-
any.whl Cython-0.26-cp27-cp27mu-manylinux1_x86_64.whl
Cython-0.26-cp35-cp35m-manylinux1_x86_64.whl decorator-4.1.2-py2.py3-none-
any.whl docutils-0.14-py2-none-any.whl docutils-0.14-py3-none-any.whl
doit-0.30.3.tar.gz dot2tex-2.9.0.tar.gz download.sh
entrypoints-0.2.3-py2.py3-none-any.whl enum34-1.1.6-py2-none-any.whl
execnet-1.4.1-py2.py3-none-any.whl fastcache-1.0.2.tar.gz
Flask-0.12.2-py2.py3-none-any.whl functools32-3.2.3-2.zip future-0.16.0.tar.gz
futures-3.1.1-py2-none-any.whl ghp_import2-1.0.1-py2.py3-none-any.whl
glfw-1.4.0.tar.gz gr-0.26.0.tar.gz holoviews-1.8.3.tar.gz
html5lib-0.999999999-py2.py3-none-any.whl husl-4.0.3.tar.gz
idna-2.6-py2.py3-none-any.whl imagesize-0.7.1-py2.py3-none-any.whl
ipykernel-4.6.1-py2-none-any.whl ipykernel-4.6.1-py3-none-any.whl
ipython-5.0.0-py2.py3-none-any.whl ipython-5.4.1-py2-none-any.whl
ipython-6.1.0-py3-none-any.whl ipython_genutils-0.2.0-py2.py3-none-any.whl
ipywidgets-7.0.0-py2.py3-none-any.whl itsdangerous-0.24.tar.gz
jedi-0.10.2-py2.py3-none-any.whl Jinja2-2.9.6-py2.py3-none-any.whl
joblib-0.11-py2.py3-none-any.whl jsonschema-2.6.0-py2.py3-none-any.whl
jupyter-1.0.0-py2.py3-none-any.whl jupyter_client-5.1.0-py2.py3-none-any.whl
jupyter_console-5.2.0-py2.py3-none-any.whl jupyter_core-4.3.0-py2.py3-none-
any.whl lancet-ioam-0.9.0.tar.gz Logbook-1.1.0.tar.gz
lxml-3.8.0-cp35-cp35m-manylinux1_x86_64.whl Mako-1.0.7.tar.gz
Markdown-2.6.9.tar.gz MarkupSafe-1.0.tar.gz matplotlib-2.0.2-cp27-cp27mu-
manylinux1_x86_64.whl matplotlib-2.0.2-cp35-cp35m-manylinux1_x86_64.whl
micawber-0.3.4.tar.gz mistune-0.7.4-py2.py3-none-any.whl mogli-0.3.0.tar.gz
mpld3-0.3.tar.gz mpmath-0.19.tar.gz natsort-5.1.0-py2.py3-none-any.whl
nbconvert-5.2.1-py2.py3-none-any.whl nbformat-4.4.0-py2.py3-none-any.whl
Nikola-7.8.9-py2.py3-none-any.whl notebook-5.0.0-py2.py3-none-any.whl
numpy-1.13.1-cp27-cp27mu-manylinux1_x86_64.whl
numpy-1.13.1-cp35-cp35m-manylinux1_x86_64.whl numpydoc-0.7.0.tar.gz
olefile-0.44.zip ordered-set-2.0.2.tar.gz pandas-0.20.3-cp27-cp27mu-
manylinux1_x86_64.whl pandas-0.20.3-cp35-cp35m-manylinux1_x86_64.whl
pandocfilters-1.4.2.tar.gz param-1.5.1.tar.gz pathlib2-2.3.0-py2.py3-none-
any.whl pathtools-0.1.2.tar.gz patsy-0.4.1-py2.py3-none-any.whl
pep8-1.7.0-py2.py3-none-any.whl periodictable-1.5.0.tar.gz
pexpect-4.2.1-py2.py3-none-any.whl phpserialize-1.3.tar.gz
pickleshare-0.7.4-py2.py3-none-any.whl piexif-1.0.12-py2.py3-none-any.whl
Pillow-4.2.1-cp35-cp35m-manylinux1_x86_64.whl pip-9.0.1-py2.py3-none-any.whl
portend-2.1.2-py2.py3-none-any.whl prompt_toolkit-1.0.15-py2-none-any.whl
prompt_toolkit-1.0.15-py3-none-any.whl ptyprocess-0.5.2-py2.py3-none-any.whl
py-1.4.34-py2.py3-none-any.whl pycodeexport-0.1.1.tar.gz
pycompilation-0.4.3.tar.gz pyflakes-1.6.0-py2.py3-none-any.whl
pygal-2.4.0-py2.py3-none-any.whl Pygments-2.2.0-py2.py3-none-any.whl
pyinotify-0.9.6.tar.gz PyLaTeX-1.2.1.tar.gz PyOpenGL-3.1.0.tar.gz
pyparsing-2.2.0-py2.py3-none-any.whl Pyphen-0.9.4-py2.py3-none-any.whl
PyRSS2Gen-1.1.tar.gz pytest-3.2.1-py2.py3-none-any.whl pytest-cache-1.0.tar.gz
pytest_cov-2.5.1-py2.py3-none-any.whl pytest_flakes-2.0.0-py2.py3-none-any.whl
pytest-pep8-1.0.6.tar.gz python2_packages.txt python3_packages.txt
python_dateutil-2.6.1-py2.py3-none-any.whl python_packages.txt
pytz-2017.2-py2.py3-none-any.whl PyYAML-3.12.tar.gz pyzmq-16.0.2-cp27-cp27mu-
manylinux1_x86_64.whl pyzmq-16.0.2-cp35-cp35m-manylinux1_x86_64.whl
qtconsole-4.3.1-py2.py3-none-any.whl quantities-0.11.1.zip
requests-2.18.4-py2.py3-none-any.whl scandir-1.5.tar.gz
scipy-0.19.1-cp27-cp27mu-manylinux1_x86_64.whl
scipy-0.19.1-cp35-cp35m-manylinux1_x86_64.whl setuptools-36.2.7-py2.py3-none-
any.whl simplegeneric-0.8.1.zip singledispatch-3.4.0.3-py2.py3-none-any.whl
six-1.10.0-py2.py3-none-any.whl smartypants-2.0.0-py2.py3-none-any.whl
snowballstemmer-1.2.1-py2.py3-none-any.whl Sphinx-1.6.3-py2.py3-none-any.whl
sphinxcontrib_websupport-1.0.1-py2.py3-none-any.whl
sphinx_rtd_theme-0.2.4-py2.py3-none-any.whl SQLAlchemy-1.1.13.tar.gz
statsmodels-0.8.0-cp27-cp27mu-manylinux1_x86_64.whl
statsmodels-0.8.0-cp35-cp35m-manylinux1_x86_64.whl stdeb-0.8.5.tar.gz
subprocess32-3.2.7.tar.gz sympy-1.1.1.tar.gz tempora-1.9-py2.py3-none-any.whl
terminado-0.6.tar.gz testpath-0.3.1-py2.py3-none-any.whl toml-0.9.2.tar.gz
toolz-0.8.2.tar.gz tornado-4.5.1.tar.gz traitlets-4.3.2-py2.py3-none-any.whl
typing-3.6.2-py2-none-any.whl typogrify-2.0.7.tar.gz
Unidecode-0.04.21-py2.py3-none-any.whl urllib3-1.22-py2.py3-none-any.whl
virtualenv-15.1.0-py2.py3-none-any.whl watchdog-0.8.3.tar.gz
wcwidth-0.1.7-py2.py3-none-any.whl webassets-0.12.1.tar.gz
webencodings-0.5.1-py2.py3-none-any.whl Werkzeug-0.12.2-py2.py3-none-any.whl
wheel-0.29.0-py2.py3-none-any.whl widgetsnbextension-3.0.2-py2.py3-none-
any.whl ws4py-0.4.2.tar.gz xarray-0.9.6-py2.py3-none-any.whl
Yapsy-1.11.223.tar.gz ; do \  
wget --quiet http://hera.physchem.kth.se/~repo/bjodahimg16/v1.3/pypi/$FNAME -O
/tmp/$FNAME; \  
done && \  
for PYPKG in cclib==1.4.1 future mako mpmath sympy pytest pytest-pep8 pytest-
cov pytest-flakes sphinx sphinx_rtd_theme periodictable pycompilation
pycodeexport numpy numpydoc scipy matplotlib pandas jupyter ipykernel cython
argh quantities fastcache bottle sqlalchemy bokeh mogli pylatex joblib toolz
statsmodels mpld3 pip stdeb param ase virtualenv xarray setuptools wheel ; do
\  
python2 -m pip install --no-index --find-links file:///tmp/ $PYPKG; \  
python3 -m pip install --no-index --find-links file:///tmp/ $PYPKG; \  
done && \  
for PYPKG in CherryPy Nikola[extras] holoviews[recommended] ipython ; do \  
python3 -m pip install --no-index --find-links file:///tmp/ $PYPKG; \  
done && \  
for PYPKG in dot2tex ipython==5 ; do \  
python2 -m pip install --no-index --find-links file:///tmp/ $PYPKG; \  
done && \  
ln -s /usr/local/share/pyphen /usr/share/pyphen && \  
python2 -m ipykernel install && \  
python3 -m ipykernel install && \  
mkdir -p /root/.config/matplotlib/ && \  
echo "backend: Agg" > /root/.config/matplotlib/matplotlibrc && \  
python2 -c "import matplotlib.pyplot as plt" && \  
python3 -c "import matplotlib.pyplot as plt" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN \  
cd /tmp && \  
for FNAME in phantomjs.tar.bz2; do \  
wget --no-verbose
"http://hera.physchem.kth.se/~repo/bjodahimg16/v1.3/blobs/$FNAME"; \  
done && \  
tar xjf phantomjs.tar.bz2 -C /usr/local/share/ && \  
ln -s /usr/local/share/phantomjs-*-linux-x86_64/bin/phantomjs /usr/local/bin/
&& \  
rm phantomjs.tar.bz2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

