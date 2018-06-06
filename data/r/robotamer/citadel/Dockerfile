FROM debian:testing  
MAINTAINER RoboTamer <gruessle@gmail.com>  
ENV O Riky.NET  
  
RUN apt-get update && \  
apt-get install -y nano rsync  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y citadel-suite && \  
apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y  
ENV DEBIAN_FRONTEND interactive  
  
EXPOSE 25/tcp 587/tcp 143/tcp 993/tcp 995/tcp 5222 2020/tcp 504/tcp 80 443  
COPY dockctrl /sbin/  
CMD ["dockctrl", "start"]  

