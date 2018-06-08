FROM debian:wheezy  
MAINTAINER simon@nostalgeek.com  
  
ADD websockify /app  
WORKDIR /app  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends python python-numpy  
  
ENTRYPOINT [ "./run" ]  

