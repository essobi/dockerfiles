FROM debian:jessie  
MAINTAINER Stephen Thirlwall <sdt@dr.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y hugs  
  
WORKDIR /hugs  
ENTRYPOINT [ "/usr/bin/hugs" ]  

