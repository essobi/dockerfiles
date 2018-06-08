FROM nginx:1.11-alpine  
MAINTAINER Stefan Gangefors <stefan@gangefors.com>  
  
ARG VERSION_REV=stable  
  
# Install build dependencies  
RUN buildDeps=' \  
git \  
' && \  
runDeps=' \  
openssl \  
' \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apk add --no-cache $buildDeps $runDeps \  
# Clone taiga-front-dist  
&& git clone https://github.com/taigaio/taiga-front-dist.git /taiga/front \  
&& cd /taiga/front \  
&& git checkout $VERSION_REV \  
# Remove build dependencies  
&& apk del --no-cache $buildDeps  
  
# Configure taiga-front-dist  
RUN openssl dhparam -out /etc/ssl/dhparam.pem 4096  
COPY nginx/* /etc/nginx/  
COPY init /taiga/init  
  
EXPOSE 80 443  
CMD ["/taiga/init"]  

