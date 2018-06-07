FROM tristansalles/docker-core:latest  
  
MAINTAINER Tristan Salles  
  
## These are for the full python - scipy stack  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends apt-utils  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
libscalapack-mpi-dev \  
libnetcdf-dev \  
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
libfreetype6-dev \  
curl \  
python-tk  
  
# (proj4 is buggered up everywhere in apt-get ... so build a known-to-work
version from source)  
RUN cd /usr/ && \  
curl http://download.osgeo.org/proj/proj-4.9.3.tar.gz > proj-4.9.3.tar.gz && \  
tar -xzf proj-4.9.3.tar.gz && \  
cd proj-4.9.3 && \  
./configure && \  
make all && \  
make install  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
--fix-missing \  
python-gdal \  
python-pil \  
libxml2-dev \  
python-lxml \  
libgeos-dev  
  
## The recent netcdf4 / pythonlibrary stuff doesn't work properly with the
default search paths etc  
## here is a fix which builds the repo version. Hoping that pip install or
apt-get install will work again soon  
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -y --no-install-recommends
python-scipy  
RUN pip install --upgrade pip && \  
pip install matplotlib numpy scipy --upgrade && \  
pip install --upgrade pyproj && \  
pip install --upgrade netcdf4  
  
RUN pip install \  
appdirs packaging \  
runipy \  
ipython \  
cmocean \  
pyevtk \  
pathlib \  
voropy \  
meshio  
  
RUN pip install --no-binary :all: shapely  
  
RUN pip install \  
pyproj \  
obspy \  
seaborn \  
pandas \  
jupyter \  
https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
\  
jupyter_nbextensions_configurator  
  
RUN pip install --upgrade cartopy  
  
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
  
### Define Jupyter environment  
RUN update-alternatives --set mpirun /usr/bin/mpirun.mpich  
  
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
WORKDIR /live  
  
# setup environment  
ENV PYTHONPATH $PYTHONPATH:/live/lib/LavaVu  
  
# get Quagmire  
WORKDIR /live/lib  
RUN git clone https://github.com/University-of-Melbourne-
Geodynamics/quagmire.git quagmire && \  
cd quagmire && \  
python setup.py build && \  
python setup.py install  
  
# get LavaVu  
WORKDIR /live/lib  
RUN git clone \--branch "1.2.14" \--single-branch
https://github.com/OKaluza/LavaVu && \  
cd LavaVu && \  
ls -k src/sqlite3 && \  
pwd && \  
make LIBPNG=1 TIFF=1 VIDEO=1 -j4 && \  
rm -fr tmp  
  
RUN cd /live/lib/ && \  
rm -rf h5py* && \  
rm -rf *.tar.gz && \  
rm -rf petsc4py-3.8.1  
  
RUN pip install shapely  
RUN pip install descartes  
RUN pip install pygmsh  
  
COPY geometry.py /live/lib  
  
RUN cd /live/lib && \  
mv geometry.py /usr/local/lib/python2.7/dist-packages/pygmsh/built_in/ && \  
git clone https://gitlab.onelab.info/gmsh/gmsh.git && \  
cd gmsh && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install && \  
cd /live/lib && \  
rm -rf gmsh  

