FROM sequenceiq/pam:ubuntu-14.04  
MAINTAINER Graeme Gellatly <graemeg@roof.co.nz>  
  
ENV DIRECTORY your.ad.domain  
ENV CLIENT_ID secret  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
# Install pam, node and freeradius  
RUN apt-get -y install software-properties-common && \  
add-apt-repository ppa:freeradius/stable && \  
apt-get update && \  
apt-get -y install --no-install-recommends \  
vim freeradius freeradius-utils nodejs nodejs-legacy npm wget  
  
RUN apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/*  
  
COPY aad-login_0.1.tar.gz /opt/  
COPY aad-login /usr/local/bin/  
# Install aad-login  
RUN cd /opt && \  
tar xzf aad-login_0.1.tar.gz -C / && \  
cd /opt/aad-login && \  
npm install && \  
chmod +x /usr/local/bin/aad-login && \  
sed -i "s|var directory = '';|var directory = ${DIRECTORY};|" aad-login.js &&
\  
sed -i "s|var clientid = '';|var clientid = ${CLIENT_ID};|" aad-login.js  
  
COPY radiusd /etc/pam.d/radiusd  
COPY ./start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
VOLUME ["/etc/freeradius"]  
  
EXPOSE 1812/udp  
EXPOSE 1812/tcp  
  
CMD /usr/local/bin/start.sh

