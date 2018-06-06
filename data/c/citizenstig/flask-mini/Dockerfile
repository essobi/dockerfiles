FROM ubuntu:14.04  
MAINTAINER Nikolay Golub <nikolay.v.golub@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y python3 python3-pip supervisor nginx && \  
pip3 install Flask==0.10.1 Flask-SQLAlchemy==2.1 Flask-Mail==0.9.1 Flask-
WTF==0.12 SQLAlchemy==1.0.12 gunicorn==19.4.5 gevent==1.1.1 && \  
apt-get clean autoclean && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log}/  
  
EXPOSE 80  
  
CMD ["/bin/true"]  

