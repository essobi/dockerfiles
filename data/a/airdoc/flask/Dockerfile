FROM ubuntu:16.04  
MAINTAINER chenmingqiang <chenmingqiang86@gmail.com>  
  
RUN chmod 777 /tmp && apt-get update && apt-get install -y redis-server
python-pip python-all python-all-dev python-dev nginx supervisor \  
automake bison flex libevent-dev libssl-dev libtool pkg-config telnet tree vim
net-tools uwsgi wget && pip install --upgrade pip \  
&& pip install redis uwsgi requests flask pillow pycrypto opencv-python qiniu
flask-mysql && pip install -v thrift==0.9.3  
  
RUN rm /etc/nginx/sites-enabled/default \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Set ~/caffe as working directory  
WORKDIR /root  
  
# start the supervisord to start the program in docker container  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

