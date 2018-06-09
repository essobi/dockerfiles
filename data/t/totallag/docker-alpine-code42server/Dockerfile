FROM anapsix/alpine-java:8_server-jre_unlimited  
MAINTAINER Chris Phan <phanx068@gmail.com>  
  
# Add s6-overlay  
ENV S6_OVERLAY_VERSION=v1.19.1.1  
# Define CrashPlanPROe server version to install  
ENV CPPE_VERSION 5.4.2  
#ENV JAVA_VERSION 7u45  
ENV JAVA_VERSION 8  
#ENV APPNAME CrashPlanPROServer  
ENV APPNAME Code42server  
  
RUN apk add --update --no-cache git tzdata musl procps coreutils && \  
apk --no-cache add --virtual devs tar curl sed bash && \  
addgroup -g 1000 app && adduser -D -G app -s /bin/false -u 1000 app && \  
curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xfz - -C /  
  
# Download and unzip installer package into /tmp/  
# RUN curl -sSL -o /tmp/jre-${JAVA_VERSION}-linux-x64.tgz
https://download.crashplan.com/installs/proserver/jre/jre-${JAVA_VERSION}-linux-x64.tgz
&& \  
RUN curl -sSL
https://download.code42.com/installs/proserver/${CPPE_VERSION}/${APPNAME}_${CPPE_VERSION}_Linux.tgz
| \  
tar -zxf - -C /tmp/ && \  
cd /tmp/${APPNAME}_${CPPE_VERSION}_Linux && \  
# Modify install.sh for silent install  
sed -i.bak 's/^\\(INSTALL_UNATTENDED=\\).*/\11/' install.sh && \  
sed -i.bak 's/^\\(AUTO_ACCEPT_EULA=\\).*/\11/' install.sh && \  
sed -i.bak 's/^\\(RUNLVLDIR=\\).*/\1\/etc\/rc2.d/' install.sh && \  
# Install the CrashPlanPROe server  
bash install.sh && \  
# Clean up to reduce layer size  
apk del devs && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Add a proserver.sh to call the bin  
RUN echo -e '#!/bin/bash \n\  
mkdir -p "/var/log/proserver" \n\  
touch "/var/log/proserver/com_backup42_app.log.0" \n\  
/opt/proserver/bin/proserver start \n\  
tail -F "/var/log/proserver/com_backup42_app.log.0"' \  
>> /proserver.sh && \  
chmod +x /proserver.sh  
  
#USER app  
# Expose all server ports (does not publish)  
EXPOSE 4280 4282 4283 4285 4286  
# Mount mutable items - logs, dbs, etc.  
VOLUME ["/var/opt/proserver/dumps","/var/log/proserver"]  
  
ENTRYPOINT ["/init"]  
  
# Define default command on container start. We tail in order to keep process
in the foreground. Logs to STDOUT  
CMD ["/proserver.sh"]  

