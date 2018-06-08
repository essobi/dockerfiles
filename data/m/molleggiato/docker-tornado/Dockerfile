FROM ubuntu:16.04  
MAINTAINER molleggiato  
  
  
# install python3.5, wget, curl, ..  
RUN apt-get update && \  
apt-get install -y --no-install-recommends software-properties-common  
  
RUN apt-get update && \  
apt-get -y install python3.5 && \  
apt-get -y install wget && \  
apt-get -y install libcurl4-openssl-dev && \  
  
apt-get -y install python3 python-dev python3-dev \  
build-essential libssl-dev libffi-dev \  
libxml2-dev libxslt1-dev zlib1g-dev \  
python-pip  
  
# install tornado framework  
RUN mkdir /home/Downloads && cd /home/Downloads  
  
RUN wget https://dl.bintray.com/pycurl/pycurl/pycurl-7.43.0.tar.gz && \  
tar -zxvf pycurl-7.43.0.tar.gz && \  
cd pycurl-7.43.0 && \  
python3 setup.py install  
  
RUN wget
https://pypi.python.org/packages/96/5d/ff472313e8f337d5acda5d56e6ea79a43583cc8771b34c85a1f458e197c3/tornado-4.4.1.tar.gz#md5=fff8a7d7f580b04bacc2ffe7ddf41133
&& \  
tar -xvzf tornado-4.4.1.tar.gz && \  
cd tornado-4.4.1 && \  
python3 setup.py build && \  
python3 setup.py install && \  
cd /  
  
# create a volume  
VOLUME ["/var/www/tornado"]  
  
# expose port  
EXPOSE 8888  
# add a startup script  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
CMD ["/start.sh"]

