FROM phusion/baseimage:0.9.15  
MAINTAINER Create Digital <hello@createdigital.me>  
  
ENV HOME /root  
CMD ["/sbin/my_init"]  
  
RUN apt-get update -qy  
RUN apt-get install -qy unzip wget software-properties-common sudo python-pip
git python-dev libxml2-dev libxslt-dev lib32z1-dev libpq-dev libjpeg8
libjpeg8-dev gettext telnet  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# LC_ALL FIX  
RUN bash -c 'echo "export LC_ALL=C.UTF-8" >> ~/.bashrc'  
  
ENV LANGUAGE C.UTF-8  
ENV PYTHONENCODING utf8  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

