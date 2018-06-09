FROM fedora:23  
MAINTAINER Julien BONACHERA <julien@bonachera.fr>  
  
RUN dnf install -y tar  
ENV URL=http://dl.4players.de/ts/releases/3.0.11.4/teamspeak3-server_linux-
amd64-3.0.11.4.tar.gz  
RUN curl -sL $URL -o /opt/ts3.tgz && \  
tar -xf /opt/ts3.tgz -C /opt && \  
useradd -r ts3 && \  
chown ts3: -R /opt/teamspeak3-server_linux-amd64/ && \  
mkdir -p /var/lib/ts3/logs /var/lib/ts3/files && \  
touch /opt/teamspeak3-server_linux-amd64/ts3server.sqlitedb && \  
chown ts3: -R /var/lib/ts3/ && \  
ln -sf /var/lib/ts3/logs /opt/teamspeak3-server_linux-amd64/logs && \  
ln -sf /var/lib/ts3/ts3server.sqlitedb /opt/teamspeak3-server_linux-
amd64/ts3server.sqlitedb && \  
ln -sf /var/lib/ts3/files /opt/teamspeak3-server_linux-amd64/files  
WORKDIR /opt/teamspeak3-server_linux-amd64/  
ENV LD_LIBRARY_PATH /opt/teamspeak3-server_linux-amd64/  
CMD /opt/teamspeak3-server_linux-amd64/ts3server_linux_amd64  

