FROM ubuntu:16.04  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y curl \  
&& curl -k -L -o /usr/local/bin/dingo
https://github.com/pforemski/dingo/releases/download/0.13/dingo-linux-amd64 \  
&& chmod a+x /usr/local/bin/dingo \  
&& apt-get remove -y --purge curl \  
&& apt-get autoremove -y --purge \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD dingo -port 53

