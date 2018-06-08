FROM ubuntu:18.04  
ADD https://s3.amazonaws.com/parsec-build/package/parsec-linux.deb parsec-
linux.deb  
RUN apt-get update && \  
apt-get -y install pulseaudio libva2 i965-va-driver libva-x11-2 && \  
dpkg -i parsec-linux.deb || true && \  
yes | apt-get -f install && \  
apt-get clean && \  
echo enable-shm=no >> /etc/pulse/client.conf && \  
useradd -ms /bin/bash parsec  
  
ENV PULSE_SERVER /run/pulse/native  
#USER parsec  
WORKDIR /home/parsec  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/parsecd"]  

