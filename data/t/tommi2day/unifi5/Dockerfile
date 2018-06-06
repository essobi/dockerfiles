FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG REPO  
  
RUN mkdir -p /usr/lib/unifi/data /backups /logs  
# add unifi repo +keys  
RUN if [ -z "$REPO" ]; then REPO="stable"; fi && \  
echo "deb http://www.ubnt.com/downloads/unifi/debian $REPO ubiquiti"
>/etc/apt/sources.list.d/ubnt.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50  
  
# update then install  
RUN apt-get update -q -y && \  
apt-get install -q -y mongodb-server unifi lsof anacron vim net-tools less  
  
#add scripts  
COPY ["unifi.sh","backup_unifi.sh","restore_unifi.sh", "/usr/lib/unifi/"]  
RUN echo "10 02 * * * root /usr/lib/unifi/backup_unifi.sh >/logs/backup.log
2>&1" >/etc/cron.d/unifi_backup  
  
# https://community.ubnt.com/t5/UniFi-Wireless-Beta/IMPORTANT-Debian-Ubuntu-
users-MUST-READ-Updated-06-21/td-p/1968253/jump-to/first-unread-message  
RUN echo "JSVC_EXTRA_OPTS=\"\$JSVC_EXTRA_OPTS -Xss1280k\""
>>/etc/default/unifi  
  
#redirect logs and backup  
RUN rm -f /usr/lib/unifi/logs && ln -s /logs /usr/lib/unifi/logs  
RUN rm -f /usr/lib/unifi/backups && ln -s /backups /usr/lib/unifi/backups  
#define interface  
VOLUME /usr/lib/unifi/data  
VOLUME /backups /logs  
EXPOSE 3748/udp 8443 8880 8080 27117  
#Runtime Env  
ENV PATH "$PATH:/usr/lib/unifi"  
WORKDIR /usr/lib/unifi  
CMD ["/usr/lib/unifi/unifi.sh", "start"]  

