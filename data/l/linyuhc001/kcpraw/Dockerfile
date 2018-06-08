FROM ubuntu  
  
  
ENV KCPRAW_VERSION 20171114  
  
RUN apt-get update -y\  
&& apt-get install -y bash libsodium-dev net-tools curl iptables\  
  
  
&& curl -sSLO
https://github.com/ccsexyz/kcpraw/releases/download/v20171114/kcpraw-linux-
amd64-$KCPRAW_VERSION.tar.gz \  
&& tar -zxf kcpraw-linux-amd64-$KCPRAW_VERSION.tar.gz \  
&& mv kcpraw_server_linux_amd64 /usr/bin/kcpraw \  
  
  
&& rm -rf kcpraw-linux-amd64-$KCPRAW_VERSION.tar.gz  
  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

