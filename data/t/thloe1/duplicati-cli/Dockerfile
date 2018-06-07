FROM mono:5  
ARG DUPLICATI_VERSION=2.0.2.1  
ARG
DUPLICATI_SHA256SUM=2b69506a39d8c15f70f7037c58d9344d08e0f6240ebcd04c4a37d6e430937453  
  
RUN cd && \  
debname="duplicati_${DUPLICATI_VERSION}-1_all.deb" && \  
curl "https://updates.duplicati.com/beta/$debname" -O && \  
echo "$DUPLICATI_SHA256SUM $debname" | sha256sum -c && \  
apt-get update && \  
{ dpkg -i "$debname" || true; } && \  
rm "$debname" && \  
apt-get install -f -y --no-install-recommends && \  
rm -r /var/lib/apt/lists/*  
  
VOLUME /mnt/db  
VOLUME /mnt/storage  
  
COPY duplicati-*.sh /usr/local/sbin/  
  
CMD ["duplicati-backup.sh"]  

