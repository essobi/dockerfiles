FROM a38y/deluge-common:1.3.10  
MAINTAINER Niels Ulrik Andersen <niels@myplace.dk>  
  
RUN apt-get update -q \  
&& apt-get install -qy \  
deluged=1.3.10-* \  
&& rm -rf /var/lib/apt/lists/* \  
;  
  
RUN /etc/init.d/deluged stop; rm /etc/init.d/deluged; update-rc.d deluged
remove  
  
ONBUILD ARG uid=1000  
ONBUILD ARG gid=$uid  
ONBUILD RUN addgroup --gid $gid user && adduser --system --home /home/user
\--uid $uid \--gid $gid \--disabled-password user  
ONBUILD USER user  
  
ONBUILD RUN \  
mkdir ~/config \  
&& ln -sfT /config/auth ~/config/auth \  
&& ln -sfT /config/core.conf ~/config/core.conf \  
&& ln -sfT /config/label.conf ~/config/label.con \  
&& ln -sfT /config/ssl ~/config/ssl \  
&& ln -sfT /config/plugins ~/config/plugins \  
&& ln -sfT /data/dht.state ~/config/dht.state \  
&& ln -sfT /data/session.state ~/config/session.state \  
&& ln -sfT /data/state ~/config/state \  
;  
  
ONBUILD VOLUME ["/config", "/data", "/logs"]  
  
ONBUILD EXPOSE 58846  
  
CMD deluged -d -c /home/user/config -l /logs/demon.log  

