#  
# Nasqueron - Phabricator image  
#  
  
FROM node  
MAINTAINER Sébastien Santoro aka Dereckson <dereckson+nasqueron-docker@espace-
win.org>  
  
RUN cd /opt && \  
git clone https://github.com/phacility/libphutil.git && \  
git clone https://github.com/phacility/phabricator.git && \  
cd phabricator/support/aphlict/server/ && \  
npm install ws && \  
groupadd -r app -g 433 && \  
mkdir /home/app && \  
useradd -u 431 -r -g app -d /home/app -s /sbin/nologin -c "Docker image user
for server" app && \  
touch /var/run/aphlict.pid /var/log/aphlict.log && \  
chown app:app /home/app /var/run/aphlict.pid /var/log/aphlict.log  
COPY aphlict.custom.json /opt/phabricator/conf/aphlict/  
  
EXPOSE 22280 22281  
  
WORKDIR /opt/phabricator/support/aphlict/server  
USER app  
CMD [ "node", "--max-old-space-size=256", "--", "aphlict_server.js", "--
config=/opt/phabricator/conf/aphlict/aphlict.custom.json" ]  

