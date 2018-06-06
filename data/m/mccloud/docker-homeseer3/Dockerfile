FROM debian  
  
RUN apt-get update && \  
apt-get install -y wget \  
mono-vbnc \  
libmono-system-web4.0.cil \  
libmono-system-design4.0.cil \  
libmono-system-web-extensions4.0-cil \  
libmono-system-runtime-caching4.0-cil \  
flite \  
chromium \  
curl  
  
RUN mkdir /src && \  
cd /src && \  
wget -O homeseer.tgz `curl -sL http://homeseer.com/current-downloads.html |
grep -Po 'http://homeseer.com/updates3/hs3_linux_3[0-9_.]+.tar.gz'`  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
VOLUME /data  
EXPOSE 80/tcp 10401/tcp 10200/tcp 10300/tcp  
  
CMD '/run.sh'  

