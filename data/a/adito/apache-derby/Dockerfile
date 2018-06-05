# Pull base image.  
FROM ubuntu:14.04.4  
  
ENV DERBY_INSTALL=/db-derby-10.12.1.1-bin  
ENV DERBY_HOME=/db-derby-10.12.1.1-bin  
ENV
CLASSPATH=/$DERBY_INSTALL/lib/derby.jar:$DERBY_INSTALL/lib/derbytools.jar:.  
  
COPY webgui/ /webgui/  
  
RUN \  
apt-get update &&\  
apt-get install -y openjdk-7-jre wget supervisor zip git curl &&\  
curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - &&\  
apt-get install -y nodejs &&\  
cd /webgui/ && /usr/bin/npm install && cd / &&\  
wget http://apache.mirror.iphh.net//db/derby/db-derby-10.12.1.1/db-
derby-10.12.1.1-bin.tar.gz &&\  
tar xzf db-derby-10.12.1.1-bin.tar.gz &&\  
rm -Rf /db-derby-10.12.1.1-bin.tar.gz &&\  
mkdir -p /dbs &&\  
mkdir -p /dbbackup &&\  
mkdir -p /upload &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
rm -Rf /etc/supervisor/supervisord.conf &&\  
touch /etc/supervisor.conf &&\  
echo "[supervisord]" >> /etc/supervisor.conf &&\  
echo "user=root" >> /etc/supervisor.conf &&\  
echo "nodaemon=true" >> /etc/supervisor.conf &&\  
echo "[rpcinterface:supervisor]" >> /etc/supervisor.conf &&\  
echo "supervisor.rpcinterface_factory =
supervisor.rpcinterface:make_main_rpcinterface" >> /etc/supervisor.conf &&\  
echo "[unix_http_server]" >> /etc/supervisor.conf &&\  
echo "file=/var/run/supervisor.sock" >> /etc/supervisor.conf &&\  
echo "chmod=0700 " >> /etc/supervisor.conf &&\  
echo "[supervisorctl]" >> /etc/supervisor.conf &&\  
echo serverurl=unix:///var/run/supervisor.sock >> /etc/supervisor.conf &&\  
echo "[program:derbydb]" >> /etc/supervisor.conf &&\  
echo "command=/bin/bash -c \"cd /dbs && /db-
derby-10.12.1.1-bin/bin/NetworkServerControl start -h 0.0.0.0 -p 1527\"" >>
/etc/supervisor.conf &&\  
echo "stopwaitsecs=30" >> /etc/supervisor.conf &&\  
echo "stopsignal=KILL" >> /etc/supervisor.conf &&\  
echo "killasgroup=true" >> /etc/supervisor.conf &&\  
echo "[program:derbywebgui]" >> /etc/supervisor.conf &&\  
echo "command=/usr/bin/node /webgui/index.js" >> /etc/supervisor.conf &&\  
echo "stopwaitsecs=30" >> /etc/supervisor.conf &&\  
echo "stopsignal=KILL" >> /etc/supervisor.conf &&\  
echo "killasgroup=true" >> /etc/supervisor.conf  
  
VOLUME ["/dbs"]  
EXPOSE 5000 1527  
CMD supervisord -c /etc/supervisor.conf  

