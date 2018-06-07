FROM ubuntu:latest  
ADD ./files/supervisor.sh /  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends curl ca-certificates \  
&& mkdir -p /opt/dropbox \  
&& curl -Lo dropbox-linux-x86_64.tar.gz
https://www.dropbox.com/download?plat=lnx.x86_64 \  
&& tar xzfv dropbox-linux-x86_64.tar.gz --strip 1 -C /opt/dropbox \  
&& rm dropbox-linux-x86_64.tar.gz \  
&& chmod +x /supervisor.sh \  
&& apt-get remove curl -y \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get purge -y \  
&& rm -rf /var/lib/apt/lists/*  
VOLUME /root/.dropbox  
ENTRYPOINT ["/supervisor.sh"]

