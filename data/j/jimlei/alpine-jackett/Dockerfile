FROM gliderlabs/alpine:latest  
  
MAINTAINER Jim Leirvik <jim@jimleirvik.no>  
  
ENV VERSION="0.6.45.2" \  
UID="1100"  
RUN adduser -D -u ${UID} jackett && \  
apk add --update openssl libcurl tar bzip2 mono --update-cache --repository
http://alpine.gliderlabs.com/alpine/edge/testing/ --allow-untrusted && \  
wget -O /tmp/jackett.tar.gz
https://github.com/raspdealer/Jackett/releases/download/v${VERSION}/Jackett.Binaries.Mono.tar.gz
&& \  
mkdir -p /config /Jackett /tmp/jackett && \  
tar -zxvf /tmp/jackett.tar.gz -C /tmp/jackett && \  
mv /tmp/jackett/Jackett-public/* /Jackett/. && \  
chown -R jackett:jackett /config /Jackett && \  
ln -s /config /usr/share/Jackett && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 9117  
VOLUME '/config'  
  
ADD start.sh /  
RUN chmod +x /start.sh  
  
WORKDIR /Jackett  
USER jackett  
  
ENTRYPOINT ["mono", "JackettConsole.exe"]  

