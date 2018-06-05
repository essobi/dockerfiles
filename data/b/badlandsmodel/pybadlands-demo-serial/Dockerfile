# Pull base image.  
FROM ubuntu:16.04  
LABEL maintainer="tristan.salles@sydney.edu.au"  
LABEL repo="https://github.com/badlands-model"  
  
# install things  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
bash-completion \  
build-essential \  
apt-utils \  
git \  
python \  
python-dev \  
python-pip \  
xorg-dev \  
ssh \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libtiff-dev \  
libxft-dev \  
xvfb \  
freeglut3 \  
freeglut3-dev \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libavcodec-dev \  
libavformat-dev \  
libavutil-dev \  
libswscale-dev \  
rsync \  
vim \  
less \  
pkg-config \  
libpng3 \  
openmpi-bin \  
libhdf5-dev \  
liblapack-dev \  
llvm-3.6 \  
libedit-dev \  
gfortran \  
libsqlite3-dev \  
xauth && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip  
RUN pip install setuptools  
  
RUN pip install \  
packaging \  
appdirs \  
numpy \  
jupyter \  
matplotlib==2.1.2. \  
runipy \  
pillow \  
enum34 \  
pyvirtualdisplay \  
scipy \  
Cython==0.20  
  
RUN pip install \  
markupsafe \  
zmq \  
singledispatch \  
backports_abc \  
certifi \  
jsonschema \  
path.py \  
git+https://github.com/badlands-model/triangle \  
pandas \  
plotly  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
libnetcdf-dev \  
xauth && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install \  
h5py \  
numba==0.23.1 \  
ez_setup \  
netcdf4 \  
colorlover \  
cmocean \  
scikit-fuzzy \  
pyevtk  
  
RUN pip install 'ipython==4.2.0' \--force-reinstall  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
wget  
#\ python-pyproj \ libproj-dev \ proj-data \ proj-bin \ libgeos-dev \ libgdal-
dev python-gdal gdal-bin  
# basemap needs compilation :((  
# though maybe you could 'pip install' it after setting the GEOS_DIR  
RUN wget http://downloads.sourceforge.net/project/matplotlib/matplotlib-
toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz && \  
tar -zxvf basemap-1.0.7.tar.gz && \  
cd basemap-1.0.7 && \  
cd geos-3.3.3 && \  
mkdir ~/install && \  
./configure --prefix=/usr/ && \  
make && \  
make install && \  
export GEOS_DIR=/usr/ && \  
cd .. && \  
python setup.py build && \  
python setup.py install && \  
cd .. && \  
rm -rf basemap-1.0.7.tar.gz && \  
rm -rf basemap-1.0.7  
  
# install things  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
sqlite3 \  
xauth && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# ^^^ Note we choose an older version of ipython because it's tooltips work
better.  
# Also, the system six is too old, so we upgrade for the pip version  
# Install Tini.. this is required because CMD (below) doesn't play nice with
notebooks for some reason: https  
#NOTE: If you are using Docker 1.13 or greater, Tini is included in Docker
itself. This includes all versions of Docker CE. To enable Tini, just pass the
--init flag to docker run.  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini >
tini && \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# script for xvfb-run. all docker commands will effectively run under this via
the entrypoint  
RUN printf "#\041/bin/sh \n rm -f /tmp/.X99-lock && xvfb-run -s '-screen 0
1600x1200x16' \$@" >> /usr/local/bin/xvfbrun.sh && \  
chmod +x /usr/local/bin/xvfbrun.sh  
  
# Add a notebook profile.  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py &&
\  
echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py  
  
# set working directory to /build  
WORKDIR /build  
  
# setup environment  
ENV PYTHONPATH $PYTHONPATH:/build/LavaVu  
  
RUN git clone https://github.com/badlands-model/pyBadlands_serial.git  
RUN mv /build/pyBadlands_serial /build/pyBadlands  
  
WORKDIR /build/pyBadlands/pyBadlands/libUtils  
RUN make  
RUN pip install -e /build/pyBadlands  
  
WORKDIR /build  
RUN git clone https://github.com/badlands-model/pyBadlands-Companion.git  
RUN pip install -e /build/pyBadlands-Companion  
  
# get LavaVu  
RUN git clone \--branch "1.2.14" \--single-branch
https://github.com/OKaluza/LavaVu && \  
cd LavaVu && \  
ls -k src/sqlite3 && \  
pwd && \  
make LIBPNG=1 TIFF=1 VIDEO=1 -j4 && \  
rm -fr tmp  
  
RUN find /build/LavaVu/notebooks -name \\*.ipynb -print0 | xargs -0 jupyter
trust && \  
mkdir /workspace && \  
mkdir /workspace/volume && \  
mkdir /workspace/companion && \  
mkdir /workspace/examples && \  
mkdir /workspace/workshop && \  
mkdir /workspace/LavaVu && \  
rsync -av /build/LavaVu/notebooks /workspace/LavaVu  
  
WORKDIR /build  
RUN git clone https://github.com/badlands-model/pyBadlands-workshop.git  
RUN cp -av /build/pyBadlands-workshop/* /workspace/workshop/  
  
# Copy test files to workspace  
RUN cp -av /build/pyBadlands/Examples/* /workspace/examples/  
RUN cp -av /build/pyBadlands-Companion/notebooks/* /workspace/companion/  
  
RUN pip install git+https://github.com/awickert/gFlex.git  
RUN pip install shapely  
RUN pip install descartes  
  
# note we also use xvfb which is required for viz  
ENTRYPOINT ["/usr/local/bin/tini", "--", "xvfbrun.sh"]  
  
# setup space for working in  
VOLUME /workspace/volume  
  
WORKDIR /workspace  
# expose notebook port  
EXPOSE 8888  
# expose LavaVu port  
EXPOSE 9999  
ENV
LD_LIBRARY_PATH=/workspace/volume/pyBadlands_serial/pyBadlands/libUtils:/build/pyBadlands/pyBadlands/libUtils  
  
# launch notebook  
CMD ["jupyter", "notebook", " --no-browser", "--allow-root", "--ip=0.0.0.0", "
--NotebookApp.iopub_data_rate_limit=1.0e10"]  

