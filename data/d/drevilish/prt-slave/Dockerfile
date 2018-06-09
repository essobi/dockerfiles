FROM linuxserver/baseimage  
  
MAINTAINER DrEVILish  
  
ENV BASE_APTLIST="build-essential git-core libssl-dev nodejs nfs-common nfs-
client rpcbind"  
# install packages  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install $BASE_APTLIST -qy && \  
npm install -g npm@latest && \  
  
# cleanup  
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
RUN cd /tmp && \  
git clone http://github.com/drevilish/node-prt && \  
cp -R /tmp/node-prt/prt-slave /app/prt-slave && \  
cd /app/prt-slave && \  
npm install && \  
chown -R abc:abc /app/prt-slave && \  
rm -rf /tmp/node-prt  
  
#Adding Custom files  
COPY init/ /etc/my_init.d/  
COPY services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh  
  
VOLUME ["/data", "/usr/lib/plexmediaserver", "/transcode","/config"]  

