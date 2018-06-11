FROM debian:wheezy  
MAINTAINER Powell Kinney <powell@vin.li>  
  
RUN apt-get update -y \  
&& apt-get install --no-install-recommends -y -q curl python build-essential
ca-certificates \  
&& mkdir /nodejs \  
&& curl https://nodejs.org/dist/v0.10.33/node-v0.10.33-linux-x64.tar.gz | tar
xvzf - -C /nodejs --strip-components=1 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH $PATH:/nodejs/bin  

