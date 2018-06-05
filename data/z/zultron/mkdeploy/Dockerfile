FROM debian:jessie  
MAINTAINER John Morris <john@zultron.com>  
  
# Set up package repos  
#  
# don't install recommended packages  
RUN echo 'APT::Install-Recommends "0";' > \  
/etc/apt/apt.conf.d/10local  
# update base image  
RUN apt-get update  
RUN apt-get upgrade -y  
# silence debconf warnings  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y libfile-fcntllock-perl  
  
# Install supervisord  
RUN apt-get install -y supervisor  
  
# Install rsyslog, esp. for ssh logging  
RUN apt-get install -y rsyslog  
RUN sed -i -e 's,/var/log/.*,/opt/aptrepo/log/syslog,' \  
/etc/rsyslog.conf  
  
# Set up ssh daemon  
RUN apt-get install -y ssh && \  
mkdir /var/run/sshd && \  
install -d -m 700 -o 1000 -g 1000 /home/docker/.ssh  
EXPOSE 22  
# Set up web server  
RUN apt-get install -y apache2  
EXPOSE 80  
RUN sed -i -e 's,/var/log/.*,/opt/aptrepo/log,' /etc/apache2/envvars  
COPY apache2.conf /etc/apache2/sites-available/000-default.conf  
  
# Install repo tools  
RUN apt-get install -y reprepro apt-transport-https ca-certificates  
  
# APT repo in /opt/aptrepo  
VOLUME /opt/aptrepo  
RUN adduser --home /opt/aptrepo --disabled-password \  
\--gecos "APT repo" \--no-create-home aptrepo  
  
# Env var: inside container  
ENV MKDOCKER_CONTAINER 1  
# Scripts in /opt/mkdocker  
VOLUME /opt/mkdocker  
WORKDIR /opt/mkdocker/mkdeploy  
CMD ["/usr/bin/supervisord", "-n", \  
"-c", "/opt/mkdocker/mkdeploy/supervisord.conf"]  

