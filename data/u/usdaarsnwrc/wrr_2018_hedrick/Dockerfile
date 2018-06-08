# SMRF is built on the IPW  
FROM usdaarsnwrc/ipw:2.4.0  
  
MAINTAINER Scott Havens <scott.havens@ars.usda.gov>  
  
####################################################  
# System requirements  
####################################################  
  
RUN echo 'Etc/UTC' > /etc/timezone \  
&& ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends libblas-dev \  
liblapack-dev \  
libatlas-base-dev \  
libffi-dev \  
libssl-dev \  
gfortran \  
libyaml-dev \  
libfreetype6-dev \  
libpng-dev \  
libhdf5-serial-dev \  
python-dev \  
python-pip \  
python-tk \  
libgrib-api-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoremove -y  
  
####################################################  
# Install SMRF and AWSM  
####################################################  
  
COPY smrf/ /code/smrf/  
COPY awsm/ /code/awsm/  
  
RUN mkdir /data \  
&& cd /code/smrf \  
&& python -m pip install --upgrade pip \  
&& python -m pip install setuptools wheel \  
&& python -m pip install -r /code/smrf/requirements.txt \  
&& python setup.py install \  
&& cd /code/awsm \  
&& python -m pip install -r /code/awsm/requirements_dev.txt \  
&& python -m pip install faulthandler \  
&& python setup.py install \  
&& rm -r /root/.cache/pip  
  
####################################################  
# Create a shared data volume  
####################################################  
  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["/bin/bash"]  
  
  
  
  
  
  
  
  
  

