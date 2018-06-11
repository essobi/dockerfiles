#  
# Copyright 2015 yafra.org  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
# yafra.org PKI docker image  
# https://github.com/yafraorg/yafra/wiki/Yapki  
#  
# source is yafra ubuntu  
FROM yafraorg/docker-yafrabase  
MAINTAINER Martin Weber <info@yafra.org>  
  
# Install common packages  
RUN \  
apk update && \  
apk upgrade && \  
apk add --update openssl openssl-dev nodejs supervisor apache2 apache2-mod-
wsgi apache2-ssl libffi libffi-dev build-base gcc && \  
# apk add --update python python-dev py-pip py-cffi  
apk add \--update python3 python3-dev  
  
# Install git repositories  
RUN \  
mkdir -p /work/repos && \  
mkdir -p /work/yafra-runtime && \  
cd /work/repos && \  
git clone https://github.com/yafraorg/yafra.git && \  
git clone https://github.com/yafraorg/yapki.git  
  
# Change default port of apache and install modules  
#RUN \  
# a2enmod cgid wsgi ssl && \  
# sed -i "/Listen/s/80/8081/" /etc/apache2/ports.conf  
# Install run script  
RUN mkdir /etc/supervisor.d  
COPY supervisord.conf /etc/supervisor.d/yapki.ini  
#COPY run-docker.sh /work/run-docker.sh  
RUN cd /work/repos/yapki/backend && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
pip3 install -r requirements.txt  
  
# Expose ports  
EXPOSE 8081  
EXPOSE 8082  
ENTRYPOINT ["/work/repos/yapki/run-docker.sh"]  
  
#CMD ["busybox /bin/bash"]  

