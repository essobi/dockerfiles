FROM debian:stable  
  
MAINTAINER minanon  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y bind9 openssl dnsutils --no-install-recommends \  
&& apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN cp -r /etc/bind /etc/bind.org  
  
EXPOSE 53/udp 53/tcp  
VOLUME [ "/etc/bind" ]  
ADD add_files/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
ENTRYPOINT [ "/start.sh" ]  

