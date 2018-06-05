FROM a38y/deluge-common:1.3.10  
MAINTAINER Niels Ulrik Andersen <niels@myplace.dk>  
  
RUN apt-get update -q \  
&& apt-get install -qy \  
deluge-web=1.3.10-* \  
&& rm -rf /var/lib/apt/lists/* \  
;  
  
ONBUILD ARG uid=1000  
ONBUILD ARG gid=$uid  
ONBUILD RUN addgroup --gid $gid user && adduser --system --home /home/user
--uid $uid \--gid $gid \--disabled-password user  
ONBUILD USER user  
ONBUILD VOLUME ["/config", "/logs"]  
  
ONBUILD EXPOSE 58846  
CMD ["deluge-web", "-c", "/config", "-l", "/logs/web.log"]  

