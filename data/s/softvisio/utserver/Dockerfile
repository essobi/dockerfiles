FROM debian:latest  
  
LABEL maintainer="zdm <zdm@softvisio.net>"  
  
USER root  
  
ADD
http://download.ap.bittorrent.com/track/beta/endpoint/utserver/os/linux-x64-debian-7-0
/var/local/utserver/utserver.tgz  
  
ADD utserver.conf /var/local/utserver/  
  
WORKDIR /var/local/utserver/  
  
RUN /bin/bash -c ' \  
apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install openssl ca-certificates wget \  
&& apt-get clean \  
  
&& tar --strip-components=1 -xzf utserver.tgz \  
&& rm -f utserver.tgz \  
&& chmod +x utserver \  
&& mkdir settings \  
'  
  
ENTRYPOINT ["/var/local/utserver/utserver", "-configfile",
"/var/local/utserver/utserver.conf", "-settingspath",
"/var/local/utserver/settings/"]  

