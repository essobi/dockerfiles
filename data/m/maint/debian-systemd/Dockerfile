FROM debian:jessie  
  
MAINTAINER Debian-Systemd Docker Maintainers <docker-maint@echip.io>  
  
LABEL description="Debian-Systemd dockerfile for everyone." vendor="HVA Team"
version="1.0"  
  
ENV \  
HOME=/root \  
  
# Let the container know that there is no tty  
DEBIAN_FRONTEND=noninteractive \  
  
container=docker  
  
WORKDIR /root  
  
COPY build/* ./.build~/  
  
RUN \  
chmod u=rwx,go= $HOME/.build~/*.sh \  
&& $HOME/.build~/000-setup.sh \  
&& rm -rf $HOME/.build~  
  
VOLUME ["/sys/fs/cgroup"]  
  
ENTRYPOINT ["/bin/systemd"]  
CMD []  
  
ONBUILD RUN apt-get update  

