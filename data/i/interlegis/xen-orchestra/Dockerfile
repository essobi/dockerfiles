FROM node:6-alpine  
MAINTAINER Fabio Rauber <fabiorauber@gmail.com>  
  
ENV REDIS_SERVER="redis" \  
REDIS_PORT="6379"  
  
LABEL xo-server=5.19.3 xo-web=5.19.1  
  
ENV USER=node USER_HOME=/home/node XOA_PLAN=5 DEBUG=xo:main  
  
WORKDIR /home/node  
RUN apk update && apk upgrade && \  
apk add --no-cache git python g++ make libc6-compat && \  
git clone -b master http://github.com/vatesfr/xen-orchestra && \  
rm -rf xen-orchestra/.git xen-orchestra/sample.config.yaml && \  
cd /home/node/xen-orchestra && yarn && yarn build && \  
# install plugins  
npm install --global \  
xo-server-auth-ldap \  
xo-server-transport-email \  
xo-server-usage-report \  
xo-server-backup-reports \  
xo-server-load-balancer \  
xo-import-servers-csv && \  
# clean a bit  
apk del git python g++ make && \  
rm -rf /root/.cache /root/.node-gyp /root/.npm  
  
COPY xo-server.config.yaml /home/node/xen-orchestra/packages/xo-server/.xo-
server.yaml  
  
EXPOSE 80  
  
ADD start.sh /usr/local/bin/start.sh  
RUN chmod a+x /usr/local/bin/start.sh  
  
CMD ["/usr/local/bin/start.sh"]  

