# VERSION 2.4.4  
FROM quay.io/keboola/base-python:3.5.1-g  
MAINTAINER Tomáš Mudruňka <mudrunka@geneea.com>  
  
# setup the environment  
WORKDIR /tmp  
RUN pip install --no-cache-dir --ignore-installed --cert=/tmp/cacert.pem \  
requests \  
&& pip install --upgrade --no-cache-dir --ignore-installed
--cert=/tmp/cacert.pem \  
git+git://github.com/keboola/python-docker-application.git@1.2.0  
  
# prepare the container  
WORKDIR /home  
COPY src src/  
  
ENTRYPOINT python ./src/main.py --data=/data  

