FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive \  
VERSION=7.6.31+dfsg-6ubuntu1  
  
RUN apt-get update \  
&& apt-get install --assume-yes --no-install-recommends \  
boinc=$VERSION \  
boinctui \  
ca-certificates \  
net-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint /entrypoint  
RUN chmod +x /entrypoint  
ENTRYPOINT ["/entrypoint"]  

