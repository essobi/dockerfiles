FROM jgiovaresco/debian-with-dockerize:latest  
MAINTAINER Julien Giovaresco <dev@giovaresco.fr>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libssl1.0.0 deluged deluge-
console unrar unzip p7zip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd --gid 1002 downloads \  
&& useradd --gid downloads deluge \  
&& mkdir /var/log/deluge /config /downloads \  
&& chown deluge:downloads /var/log/deluge /config /downloads \  
&& chmod 775 -R /var/log/deluge /config /downloads  
  
USER deluge  
  
EXPOSE 58846  
VOLUME ["/config", "/downloads"]  
  
ADD core.conf /home/deluge/core.conf  
ADD auth.tmpl /home/deluge/auth.tmpl  
  
CMD dockerize \  
-template /home/deluge/core.conf:/config/core.conf \  
-template /home/deluge/auth.tmpl:/config/auth \  
-stdout /var/log/deluge/deluge.log \  
deluged -d --config /config -l /var/log/deluge/deluge.log -L warning

