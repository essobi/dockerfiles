FROM ubuntu:14.04  
MAINTAINER Hemslo Wang <hemslo.wang@gmail.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7  
RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee
/etc/apt/sources.list.d/scrapy.list  
RUN apt-get update && apt-get install -y \  
python python-dev python-distribute python-pip scrapy-0.24 scrapyd  
  
ADD requirements.txt /src/requirements.txt  
RUN pip install -r /src/requirements.txt  
  
VOLUME ["/var/log/scrapyd", "/var/lib/scrapyd"]  
  
EXPOSE 6800  
CMD ["/usr/bin/scrapyd"]  

