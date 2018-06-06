FROM ubuntu:14.04  
MAINTAINER Dockerfiles  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing && apt-get
install -y build-essential git python3 python3-dev python3-setuptools nginx
supervisor bcrypt libssl-dev libffi-dev libpq-dev vim redis-server rsyslog
wget  
RUN easy_install3 pip  
  
# install our code  
ADD . /home/docker/code/  
  
# run pip install  
RUN pip3 install -U -r /home/docker/code/requirements.txt  
  
WORKDIR /home/docker/code  
  
expose 5000  
CMD ["/usr/local/bin/uwsgi", "--ini", "/home/docker/code/uwsgi.ini"]

