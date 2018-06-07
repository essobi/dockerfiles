# docker for the MVA course  
FROM ubuntu:xenial  
MAINTAINER Gabriele Facciolo <gfacciol@gmail.com>, Carlo de Franchis
<carlodef@gmail.com>  
RUN apt-get update && apt-get install -y software-properties-common  
RUN apt-add-repository -y ppa:ubuntugis/ppa  
RUN apt-get update && apt-get install -y \  
build-essential \  
gdal-bin \  
geographiclib-tools \  
git \  
libfftw3-dev \  
libgdal-dev \  
libgeographic-dev \  
libgeotiff-dev \  
libtiff5-dev \  
npm \  
nodejs-legacy \  
python3 \  
python3-gdal \  
python3-pip \  
python3-numpy-dev \  
software-properties-common \  
imagemagick \  
vim  
RUN add-apt-repository ppa:certbot/certbot -y  
  
# https stuff: TODO manually in interactive mode  
# apt-get update & apt-get install certbot  
# certbot certonly --register-unsafely-without-email  
# install jupyterhub  
RUN pip3 install -U pip  
RUN pip3 install jupyter jupyterhub notebook  
RUN npm install -g configurable-http-proxy  
  
# install TSD requirements  
RUN git clone https://github.com/carlodef/tsd.git --branch master --single-
branch --depth 1 --recursive  
RUN pip3 install -r tsd/requirements.txt  
  
RUN pip3 install matplotlib scipy  
  
# install widget stuff  
RUN pip3 install \  
pandas \  
folium \  
ipywidgets \  
ipyleaflet && \  
jupyter nbextension enable \--py --sys-prefix widgetsnbextension && \  
jupyter nbextension enable \--py --sys-prefix ipyleaflet  
  
RUN pip install jupyterhub-systemdspawner  
# missing  
RUN pip3 install scikit-image \  
numba pillow \  
opencv-contrib-python \  
ad  
RUN pip3 install --upgrade scipy  
  
# create user accounts  
#RUN useradd -m -p $(openssl passwd -1 ed188d37503aa2fe3cd65bc51516c41a) carlo  
RUN useradd -m -p $(openssl passwd -1 password) student1  
  
# export jupyter to pdf  
RUN apt-get update && apt-get install -y \  
pandoc \  
texlive-xetex \  
unzip  
  

