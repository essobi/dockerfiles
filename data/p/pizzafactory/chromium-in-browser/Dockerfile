FROM quantumobject/docker-baseimage  
MAINTAINER Masaki Muranaka <monaka@monami-ya.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install chromium-browser \  
x11vnc xvfb \  
guacamole guacamole-tomcat && \  
apt-get -y autoremove && \  
apt-get -y clean  
  
RUN mkdir /etc/service/chromium-browser  
COPY chromium-browser.sh /etc/service/chromium-browser/run  
  
RUN mkdir /etc/service/x11vnc  
COPY x11vnc.sh /etc/service/x11vnc/run  
  
RUN mkdir /etc/service/xvfb  
COPY xvfb.sh /etc/service/xvfb/run  
  
RUN mkdir /etc/service/guacamole  
COPY guacamole.sh /etc/service/guacamole/run  
  
RUN mkdir /etc/service/guacd  
COPY guacd.sh /etc/service/guacd/run  
  
EXPOSE 8080  
CMD ["/sbin/my_init"]  

