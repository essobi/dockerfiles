FROM debian:stretch-slim  
  
MAINTAINER calvintam236 <calvintam236@users.noreply.github.com>  
LABEL description="ElectroneumD in Docker. Full node. Supports CPU mining."  
  
WORKDIR /tmp  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install ca-certificates curl unzip \  
&& curl -L -O
https://github.com/electroneum/electroneum/releases/download/v0.11.0.0-revert/linux-x64-v0.11.0.0-revert.zip
\  
&& unzip linux-x64-v0.11.0.0-revert.zip \  
&& rm linux-x64-v0.11.0.0-revert.zip \  
&& mv electroneumd /usr/local/bin/electroneumd \  
&& chmod a+x /usr/local/bin/electroneumd \  
&& rm -r * \  
&& apt-get -y remove ca-certificates curl unzip \  
&& apt-get -y autoremove \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
ENTRYPOINT ["electroneumd"]  
CMD ["--help"]  

