FROM frolvlad/alpine-mono  
# MAINTAINER Katalina T. <docker-gtan@kat.cafe>  
EXPOSE 4499/udp  
WORKDIR /srv  
  
RUN apk add --no-cache unzip su-exec curl && \  
# adduser -S gtan && \  
curl https://download.gtanet.work/server/latest.zip > /srv/gtanserver.zip && \  
cd /srv && \  
unzip gtanserver.zip && \  
rm gtanserver.zip  
  
CMD ash -c '(cd /srv; mono GTANetworkServer.exe)'

