FROM gitlab/dind  
  
ENV DIP_VERSION 2.0.0  
RUN apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
make \  
libyaml-0-2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& truncate -s 0 /var/log/*log  
  
RUN curl -L https://github.com/bibendi/dip/releases/download/$DIP_VERSION/dip-
Linux-x86_64 > /usr/local/bin/dip \  
&& chmod +x /usr/local/bin/dip  
  
ADD prepare-build /usr/local/bin/  
ADD fetch-images /usr/local/bin/  

