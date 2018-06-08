FROM debian:jessie  
MAINTAINER Andre Schurer <aschurer@statix.nl>  
  
ADD http://repo.owntracks.org/repo.owntracks.org.gpg.key
/tmp/owntracks.gpg.key  
RUN apt-key add /tmp/owntracks.gpg.key && \  
apt-get update && \  
apt-get install -y software-properties-common net-tools && \  
apt-add-repository 'deb http://repo.owntracks.org/debian jessie main' && \  
apt-get update && \  
apt-get install -y \  
libsodium13 \  
libcurl3 \  
liblua5.2-0 \  
supervisor \  
ot-recorder \  
curl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /owntracks  
  
COPY ot-recorder.default /etc/default/ot-recorder  
  
COPY launcher.sh /usr/local/sbin/launcher.sh  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY recorder-health.sh /usr/local/sbin/recorder-health.sh  
HEALTHCHECK CMD /usr/local/sbin/recorder-health.sh  
  
RUN mkdir -p /var/log/supervisor && \  
mkdir -p -m 775 /owntracks/recorder/store && \  
chown -R owntracks:owntracks /owntracks && \  
chmod 755 /usr/local/sbin/launcher.sh /usr/local/sbin/recorder-health.sh  
  
EXPOSE 8083  
CMD ["/usr/local/sbin/launcher.sh"]  

