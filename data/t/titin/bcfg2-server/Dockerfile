FROM debian:stretch  
MAINTAINER Corentin Bonneton <contact@feelb.io>  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TERM="xterm"  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup &&\  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
apt-get -q update && \  
apt-get -qy dist-upgrade && \  
apt-get install -qy \  
ca-certificates \  
supervisor \  
pwgen \  
bcfg2-server \  
&& \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD bcfg2.conf /etc/bcfg2/bcfg2.conf  
  
VOLUME /var/lib/bcfg2  
VOLUME /etc/bcfg2/  
  
EXPOSE 6789  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD start.sh /start.sh  
  
CMD ["/start.sh"]  

