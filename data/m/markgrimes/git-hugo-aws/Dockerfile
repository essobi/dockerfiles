FROM debian:jessie-slim  
  
  
# Install git straight from apt  
RUN apt-get update -y \  
&& apt-get install -y git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install aws and all its dependencies  
RUN apt-get update \  
&& apt-get install -y python-pip \  
&& pip install awscli \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Download and install Hugo  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -L
https://github.com/gohugoio/hugo/releases/download/v0.32.2/hugo_0.32.2_Linux-64bit.deb
> /tmp/hugo.deb \  
&& dpkg -i /tmp/hugo.deb \  
&& rm /tmp/hugo.deb \  
&& apt-get autoremove -y curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

