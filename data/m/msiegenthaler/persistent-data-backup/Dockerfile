FROM debian:8.6  
MAINTAINER Mario Siegenthaler <mario.siegenthaler@linkyard.ch>  
  
# Add Tini  
ENV TINI_VERSION v0.13.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Install backup-ninja  
RUN apt-get update && \  
apt-get install -y duplicity backupninja && \  
rm -rf /var/lib/apt/lists/*  
  
COPY 10.dup /etc/backup.d/  
RUN chmod 600 /etc/backup.d/10.dup  
  
# Will be backuped  
VOLUME [ "/data" ]  
# Where the backup goes to  
VOLUME [ "/backup-target" ]  
  
COPY run.sh /  
CMD [ "/run.sh" ]  

