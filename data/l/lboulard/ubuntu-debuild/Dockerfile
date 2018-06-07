FROM lboulard/ubuntu-dev:bionic  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y gosu  
  
ARG tiny_pkg=tini_0.17.0-amd64.deb  
COPY $tiny_pkg /  
RUN dpkg -i /$tiny_pkg && rm -f /$tiny_pkg  
  
ADD debuild-entrypoint.sh /sbin/entrypoint.sh  
  
ENTRYPOINT [ "/sbin/entrypoint.sh" ]  

