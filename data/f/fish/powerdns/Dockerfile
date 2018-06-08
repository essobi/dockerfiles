FROM ubuntu:14.04  
MAINTAINER Johannes 'fish' Ziemke <docker@freigeist.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y -q install \  
pdns-backend-mysql pdns-backend-pgsql pdns-backend-sqlite3  
  
EXPOSE 53  
ENTRYPOINT [ "/usr/sbin/pdns_server" ]  
CMD [ "--no-config", "--master", "--daemon=no", \  
"--local-address=0.0.0.0", \  
"--allow-axfr-ips=${PDNS_AXFR_IPS:-127.0.0.0/8}" ]  

