FROM debian  
  
RUN apt-get update \  
&& apt-get -y install \  
bash \  
dnsutils \  
traceroute \  
tcptraceroute \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

