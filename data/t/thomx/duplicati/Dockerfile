FROM mono:4  
MAINTAINER Thomas M "maugin.thomas@gmail.com"  
ENV DUPLICATI_VER 2.0.3.2_canary_2018-03-16  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
RUN echo 'Acquire::ForceIPv4 "true";' | tee /etc/apt/apt.conf.d/99force-ipv4
&& \  
apt-get update && \  
apt-get -y -o Dpkg::Options::="--force-confold" install --no-install-
recommends \  
expect \  
libsqlite3-0 \  
unzip \  
locales && \  
curl -sSL https://updates.duplicati.com/canary/duplicati-${DUPLICATI_VER}.zip
-o /duplicati-${DUPLICATI_VER}.zip && \  
unzip duplicati-${DUPLICATI_VER}.zip -d /app && \  
rm /duplicati-${DUPLICATI_VER}.zip && \  
apt-get purge -y --auto-remove unzip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# create duplicati user and folder  
RUN useradd -u 911 -s /bin/false duplicati && \  
usermod -G users duplicati  
RUN mkdir -p /home/duplicati/.config/Duplicati  
  
# add local files  
COPY root/ /  
  
VOLUME /home/duplicati/.config/Duplicati  
  
EXPOSE 8200  
ENTRYPOINT ["/init"]  
  

