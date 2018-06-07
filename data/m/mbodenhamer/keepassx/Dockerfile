FROM debian:jessie  
MAINTAINER Matt Bodenhamer <mbodenhamer@mbodenhamer.com>  
  
RUN apt-get update && apt-get install -y \  
keepassx \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV QT_X11_NO_MITSHM=1  
VOLUME /files  
WORKDIR /files  
ENTRYPOINT ["keepassx"]  

