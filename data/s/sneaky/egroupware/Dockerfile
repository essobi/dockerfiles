FROM sneaky/egroupware:basis  
MAINTAINER André Scholz <info@rothaarsystems.de>  
# Version 2017-12-03-21-30  
ENV DEBIAN_FRONTEND noninteractive  
ARG egr_timezone=Europe/Berlin  
# start egroupware installation  
RUN echo 'deb
http://download.opensuse.org/repositories/server:/eGroupWare/Debian_9.0/ /' >
/etc/apt/sources.list.d/egroupware-epl.list \  
&& wget -nv
https://download.opensuse.org/repositories/server:eGroupWare/Debian_9.0/Release.key
-O Release.key \  
&& apt-key add - < Release.key \  
&& apt-get update \  
&& apt-get install -y egroupware-epl  
  
COPY assets/docker-entrypoint.sh /bin/entrypoint.sh  
  
# there are two updated files  
# because manual installation of egroupware leaves some infos blank  
COPY assets/class*.* /usr/share/egroupware/setup/inc/  
  
RUN chmod +x /bin/entrypoint.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/bin/entrypoint.sh"]  
CMD ["app:start"]

