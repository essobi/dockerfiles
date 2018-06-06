FROM pdal/pdal:1.5  
MAINTAINER Max Burnette <mburnet2@illinois.edu>  
  
# Install any programs needed  
RUN useradd -u 49044 extractor \  
&& mkdir -p /home/extractor/sites/ua-mac/raw_data \  
&& mkdir -p /home/extractor/sites/ua-mac/Level_1/scanner3DTop \  
&& mkdir -p /home/extractor/sites/ua-mac/Level_1/scanner3DTop_mergedlas \  
&& chown -R extractor /home/extractor \  
# Requirements for terrautils  
&& apt-get -q -y update \  
&& apt-get install -y --no-install-recommends build-essential \  
software-properties-common \  
gcc make wget byacc \  
libpng-dev \  
libjpeg8-dev \  
libfreetype6-dev \  
libnetcdf-dev \  
libhdf5-dev \  
libblas-dev \  
liblapack-dev \  
libatlas-base-dev \  
libgdal-dev \  
python-dev \  
python-tk \  
# Requirements for pyclowder  
netcat \  
python \  
python-pip \  
git \  
&& add-apt-repository ppa:ubuntugis/ubuntugis-unstable \  
&& apt-get -q -y update \  
&& apt-get install -y python-gdal \  
&& pip install --upgrade setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install pyclowder  
RUN cd /home/extractor \  
&& git clone
https://opensource.ncsa.illinois.edu/bitbucket/scm/cats/pyclowder2.git \  
&& pip install --upgrade -r pyclowder2/requirements.txt \  
&& pip install --upgrade /home/extractor/pyclowder2  
  
# Install terrautils  
RUN cd /home/extractor \  
&& git clone https://github.com/terraref/terrautils.git \  
&& pip install --upgrade -r terrautils/requirements.txt \  
&& pip install --upgrade /home/extractor/terrautils \  
&& pip install laspy  
  
# command to run when starting docker  
COPY entrypoint.sh extractor_info.json *.py /home/extractor/  
  
USER extractor  
ENTRYPOINT ["/home/extractor/entrypoint.sh"]  
CMD ["extractor"]  
  
# Setup environment variables. These are passed into the container. You can
change  
# these to your setup. If RABBITMQ_URI is not set, it will try and use the
rabbitmq  
# server that is linked into the container. MAIN_SCRIPT is set to the script
to be  
# executed by entrypoint.sh  
ENV RABBITMQ_EXCHANGE="terra" \  
RABBITMQ_VHOST="%2F" \  
RABBITMQ_QUEUE="terra.ply2las" \  
RABBITMQ_URI="" \  
MAIN_SCRIPT="terra_ply2las.py"  

