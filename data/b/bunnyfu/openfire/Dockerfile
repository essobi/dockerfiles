FROM sameersbn/ubuntu:14.04.20160827  
MAINTAINER sameer@damagehead.com  
  
ENV OPENFIRE_VERSION=4.0.3 \  
OPENFIRE_USER=openfire \  
OPENFIRE_DATA_DIR=/var/lib/openfire \  
OPENFIRE_LOG_DIR=/var/log/openfire  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-7-jre  
RUN cd /tmp && wget
http://download.igniterealtime.org/openfire/openfire_4.0.3_all.deb  
RUN dpkg -i openfire_4.0.3_all.deb  
RUN mv /var/lib/openfire/plugins/admin /usr/share/openfire/plugin-admin  
RUN rm -rf openfire_4.0.3_all.deb  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 3478/tcp 3479/tcp 5222/tcp 5223/tcp 5229/tcp 7070/tcp 7443/tcp 7777/tcp
9090/tcp 9091/tcp  
VOLUME ["${OPENFIRE_DATA_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

