FROM shimaore/docker.freeswitch  
MAINTAINER Stéphane Alnet <stephane@shimaore.net>  
ENV NODE_ENV production  
ENV SPOOL /opt/freeswitch/var/spool  
  
USER root  
RUN \  
mkdir -p /opt/gabby-potato/conf /opt/gabby-potato/log && \  
chown -R freeswitch.freeswitch /opt/gabby-potato/ && \  
apt-get update && apt-get install -y \--no-install-recommends \  
ca-certificates \  
curl \  
git \  
make \  
&& \  
# Install Node.js using `n`.  
git clone https://github.com/tj/n.git n.git && \  
cd n.git && \  
make install && \  
cd .. && \  
rm -rf n.git && \  
n 9.11.1 && \  
apt-get purge -y \  
ca-certificates \  
curl \  
git \  
make \  
&& \  
apt-get autoremove -y && apt-get clean && \  
rm -rf /usr/share/man /var/log/lastlog /tmp/*  
  
WORKDIR /opt/gabby-potato  
USER freeswitch  
COPY . /opt/gabby-potato/  
RUN \  
npm install && \  
npm cache clean --force && \  
rm -rf \  
/home/freeswitch/.node-gyp \  
/opt/freeswitch/etc/freeswitch/* \  
/opt/freeswtch/include/freeswitch \  
/opt/freeswitch/share/freeswitch/fonts \  
/opt/freeswitch/htdocs && \  
mkdir -p ${SPOOL}/fax \  
${SPOOL}/modem  
  
# 8021: FreeSwitch event socket  
# 3000: Axon publisher (notifies of new inbound calls)  
# 3001: Axon subscriber (submit commands to the calls)  
EXPOSE 8021 3000 3001  
ENTRYPOINT ["node","server.js"]  
CMD ["{}"]  

