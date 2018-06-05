# py-ubuntu 0.9  
# 192.168.99.100  
FROM ubuntu:15.10  
MAINTAINER Jonel Rienton jonel@road14.com  
  
RUN apt-get -y update && apt-get install -y python3.5 python3.5-dev
libcurl4-openssl-dev  
  
RUN ln -s /usr/bin/python3.5 /usr/bin/python  
  
COPY get-pip.py /tmp/get-pip.py  
  
RUN /bin/mkdir /webapps  
  
ENV webapp /webapps  
  
ENV flaskapp ${webapp}/flaskweb  
  
WORKDIR ${webapp}  
  
ADD flaskweb.tar.gz .  
  
WORKDIR ${flaskapp}  
  
ADD venv.tar.gz .  
  
RUN . venv/bin/activate  
  
RUN mkdir instance && rm -rf .git  
  
COPY config.py instance/config.py  
  
EXPOSE 80  
CMD venv/bin/uwsgi --socket 0.0.0.0:80 -w wsgi --master --process 4 --protocol
http --gid 33

