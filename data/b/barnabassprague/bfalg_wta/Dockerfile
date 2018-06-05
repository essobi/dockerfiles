# Copyright 2017, RadiantBlue Technologies, Inc.  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
# http://www.apache.org/licenses/LICENSE-2.0  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM debian:latest  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /work  
  
RUN apt-get update; \  
apt-get install -y python-setuptools python-numpy python-dev libgdal-dev
python-gdal swig git g++; \  
apt-get install -y libagg-dev libpotrace-dev; \  
easy_install pip; pip install wheel;  
  
COPY requirements.txt /work/requirements.txt  
  
RUN \  
pip install cython; \  
pip install -r requirements.txt  
RUN pip install nose==1.3.7  
  
RUN git clone -b develop https://github.com/venicegeo/bfalg_WTA  
WORKDIR /work/bfalg_WTA  
RUN python setup.py sdist  
RUN python setup.py install  
WORKDIR /work  
RUN cp /work/bfalg_WTA/WTA/bfalg_WTA.py /usr/local/bin  
RUN chmod 7777 /usr/local/bin/bfalg_WTA.py  
RUN cp -r bfalg_WTA/WTA/* /work  
RUN mkdir data  
#RUN nosetests  
CMD /bin/bash  
  

