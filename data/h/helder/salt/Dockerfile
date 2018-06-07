FROM debian:jessie  
LABEL maintainer=helder  
  
RUN apt-get update \  
&& apt-get install wget ca-certificates --no-install-recommends -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -O - https://repo.saltstack.com/apt/debian/8/amd64/latest/SALTSTACK-
GPG-KEY.pub | apt-key add - \  
&& echo 'deb http://repo.saltstack.com/apt/debian/8/amd64/latest jessie main'
>> /etc/apt/sources.list.d/saltstack.list \  
&& apt-get update \  
&& apt-get install -y salt-master \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4505 4506  
VOLUME /etc/salt /var/cache/salt /var/log/salt /var/run/salt  
CMD ["/usr/bin/salt-master"]  

