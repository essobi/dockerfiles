FROM ubuntu:14.04  
# Install binary dependencies  
RUN apt-get -qqy update && \  
apt-get install -qqy software-properties-common --no-install-recommends && \  
apt-add-repository -y ppa:ubuntugis/ppa && \  
apt-get install -qqy \  
wget \  
curl \  
build-essential \  
gdal-bin \  
libgdal-dev \  
libspatialindex-dev \  
python \  
python-dev \  
python-tk \  
idle \  
python-pmw \  
python-imaging \  
python-opencv \  
python-matplotlib \  
git-all \  
\--no-install-recommends  
  
#RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
# wget --quiet
https://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh -O
~/anaconda.sh && \  
# /bin/bash ~/anaconda.sh -b -p /opt/conda && \  
# rm ~/anaconda.sh  
# Install pip since a known issue on pip installation in trusty 14.04  
# https://github.com/tethysplatform/tethys/issues/231  
  
RUN curl -s "https://bootstrap.pypa.io/get-pip.py" | python  
  
RUN apt-add-repository ppa:ubuntugis/ubuntugis-unstable  
  
RUN apt-get update  
  
RUN apt-get -qqy install python-gdal  
  
RUN pip install geojson && \  
pip install shapely && \  
pip install ipython && \  
pip install jupyter && \  
pip install pandas && \  
pip install tifffile && \  
pip install scikit-learn && \  
pip install scipy && \  
pip install descartes && \  
pip install awscli --ignore-installed six && \  
pip install plotly  
  
# Fix error  
RUN ln /dev/null /dev/raw1394  
  
# Clean-up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

