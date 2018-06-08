FROM ubuntu:16.04  
MAINTAINER Georges Haidar <georges.haidar@myob.com>  
  
COPY scripts/* /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/* \  
&& mkdir -p /home/appuser \  
&& groupadd -g 1000 appuser \  
&& useradd -g appuser -d /home/appuser -u 1000 -s /bin/bash appuser \  
&& chown appuser:appuser /home/appuser \  
&& apt-get update \  
&& apt-get upgrade -y --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& find / -xdev -perm /6000 -type f -exec chmod a-s {} \;  
  
ENTRYPOINT ["dumb-init"]  

