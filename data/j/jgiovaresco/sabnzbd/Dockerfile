FROM jgiovaresco/debian-with-dockerize:latest  
MAINTAINER Julien Giovaresco <dev@giovaresco.fr>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends python python-cheetah python-
yenc python-service-identity unrar unzip p7zip par2 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd --gid 1002 downloads \  
&& useradd --home-dir /home/sabnzbd --gid downloads --create-home sabnzbd \  
&& mkdir /var/log/sabnzbd /config /downloads \  
&& chown sabnzbd:downloads /var/log/sabnzbd /config /downloads \  
&& chmod 775 -R /var/log/sabnzbd /config /downloads  
  
USER sabnzbd  
WORKDIR /home/sabnzbd  
  
ENV VERSION 1.0.3  
RUN wget --no-check-certificate -O sabnzbd.tar.gz
https://github.com/sabnzbd/sabnzbd/releases/download/${VERSION}/SABnzbd-${VERSION}-src.tar.gz
\  
&& tar xvfz sabnzbd.tar.gz \  
&& rm -rf sabnzbd.tar.gz  
  
EXPOSE 8080 9090  
VOLUME ["/config", "/downloads"]  
  
CMD dockerize \  
-stdout /var/log/sabnzbd/sabnzbd.log \  
python SABnzbd-${VERSION}/SABnzbd.py --config-file /config --logging 1 -s
0.0.0.0:8080  

