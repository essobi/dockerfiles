FROM debian  
  
RUN \  
echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen'
> /etc/apt/sources.list.d/mongodb.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y curl git supervisor mongodb-
org && \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs && \  
apt-get clean  
  
RUN git clone https://github.com/volpe28v/DevHub.git && \  
cd DevHub && \  
npm install  
  
RUN ( \  
echo "[program:devhub]" && \  
echo "command=/usr/bin/node /DevHub/app.js" && \  
echo "directory=/DevHub" && \  
echo "user=nobody" && \  
echo "autostart=true" && \  
echo "redirect_stderr=true" && \  
echo "stderr_logfile = /DevHub/err.log" && \  
echo "stdout_logfile = /DevHub/out.log" && \  
echo "[program:mongodb]" && \  
echo "command=/usr/bin/mongod --config /etc/mongod.conf" && \  
echo "user=mongodb" && \  
echo "autostart=true" && \  
echo "redirect_stderr=true" \  
) > /etc/supervisor/conf.d/devhub.conf  
  
EXPOSE 3000  
VOLUME ["/DevHub", "/var/lib/mongodb"]  
  
ENTRYPOINT ["/usr/bin/supervisord", "-n"]  

