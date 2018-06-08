# vim: set filetype=dockerfile  
FROM limed/ubuntu-base:16.04  
MAINTAINER limed@sudoers.org  
  
RUN add-apt-repository -y ppa:jcfp/ppa \  
&& add-apt-repository -y ppa:jcfp/sab-addons \  
&& apt-get -q update \  
&& apt-get install --no-install-recommends -qy sabnzbdplus\  
par2-tbb \  
python-sabyenc \  
python-cryptography \  
unzip \  
unrar \  
p7zip-full \  
locales \  
&& locale-gen "en_US.UTF-8" \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& mkdir -p /config \  
&& mkdir -p /data/sabnzbd/downloads \  
&& mkdir -p /data/sabnzbd/nzb \  
&& chmod 777 /data/sabnzbd/downloads  
  
# Other volumes here  
VOLUME [ "/config", "/data/sabnzbd/downloads", "/data/sabnzbd/nzb" ]  
  
# copy supervisord  
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 8080  
EXPOSE 9090  
  
CMD [ "/usr/bin/supervisord" ]  

