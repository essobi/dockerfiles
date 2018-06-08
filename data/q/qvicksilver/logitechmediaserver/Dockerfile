FROM debian:jessie  
MAINTAINER Jonathan Süssemilch Poulain <jonathan@sofiero.net>  
  
SHELL [ "/bin/bash", "-c" ]  
  
ENV LANG=C.UTF-8 \  
update_url="http://www.mysqueezebox.com/update/?version=7.9.0&revision=1&geturl=1&os=deb"  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install \  
curl \  
faad \  
flac \  
lame \  
perl \  
sox \  
wget \  
libio-socket-ssl-perl \  
libnet-ssleay-perl \  
&& \  
rm -rf /var/lib/apt/lists/* && \  
download_url=$(curl -Lsf "$update_url") && \  
download_url=${download_url/_all/_amd64} && \  
curl -Lsf -o /tmp/logitechmediaserver.deb $download_url && \  
DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/logitechmediaserver.deb && \  
rm -f /tmp/logitechmediaserver.deb  
  
EXPOSE 3483 3483/udp 9000 9090  
COPY entrypoint.sh /  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "" ]  

