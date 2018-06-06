### This file can be used to build a docker image like this:  
### docker build --tag='test1' .  
### It can also be used for automated builds in Docker Hub  
### (see https://docs.docker.com/userguide/dockerrepos/#automated-builds)  
FROM ubuntu:14.04  
MAINTAINER Dashamir Hoxha dashohoxha@gmail.com  
  
COPY . /usr/local/src/p2p/  
ENV code_dir /usr/local/src/p2p  
WORKDIR /usr/local/src/p2p/  
RUN ["install/install-container.sh", "install/settings.sh"]  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "--
nodaemon"]  

