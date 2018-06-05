FROM debian:jessie  
  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
locales \  
hledger \  
hledger-web \  
&& locale-gen C.UTF-8 \  
&& echo 'C.UTF-8 UTF-8' > /etc/locale.gen \  
&& locale-gen C.UTF-8 \  
&& dpkg-reconfigure locales \  
&& /usr/sbin/update-locale LANG=C.UTF-8 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LC_ALL C.UTF-8  
COPY data /data  
VOLUME /data  
  
EXPOSE 5000  
COPY start.sh /start.sh  
  
CMD ["/start.sh"]  

