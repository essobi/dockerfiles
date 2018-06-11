FROM ubuntu:14.04  
MAINTAINER Benoit Beausejour <b@turbulent.ca>  
  
ENV heap-base 2.0.3  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "#deb http://archive.ubuntu.com/ubuntu/ trusty-proposed main
restricted" > /etc/apt/sources.list.d/proposed.list  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y ssmtp && \  
apt-get install -y bsd-mailx && \  
apt-get -y install supervisor && \  
apt-get install -y python-pip && \  
apt-get install -y python-yaml && \  
pip install pystache && \  
pip install Jinja2 && \  
apt-get -y install apt-transport-https && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
echo "deb https://get.docker.com/ubuntu docker main" >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get -y install lxc-docker-1.6.0 && \  
(adduser --system --uid 1000 \--gid 33 \--home /home/heap --shell /bin/bash
heap) && \  
usermod -G docker heap && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get -y clean  
  
ADD systpl.mustache.py /systpl/  
ADD systpl.jinja.py /systpl/  
RUN ln -s /systpl/systpl.mustache.py /systpl/systpl.py  
  
COPY ssmtp.conf.tmpl /systpl/  
  
ENV VAR_SSMTP_ROOT_ALIAS "sys@turbulent.ca"  
ENV VAR_SSMTP_MAILHUB "localhost"  
ENV VAR_SSMTP_HOSTNAME "localhost"  
ENV VAR_SSMTP_SSL "1"  
ENV VAR_SSMTP_AUTH_USERNAME ""  
ENV VAR_SSMTP_AUTH_PASSWORD ""  
CMD []  
ENTRYPOINT []  

