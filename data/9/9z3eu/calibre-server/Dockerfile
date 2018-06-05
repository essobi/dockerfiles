FROM ubuntu:17.10  
MAINTAINER stef@9z3.eu  
  
RUN apt-get update -y \  
&& apt-get install -y calibre \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  
EXPOSE 8080  
RUN mkdir /opt/calibre && mkdir /opt/calibre/library && mkdir
/opt/calibre/config  
  
VOLUME ["/opt/calibre/library"]  
VOLUME ["/opt/calibre/config"]  
  
ENTRYPOINT ["/usr/bin/calibre-server", "/opt/calibre/library"]  
  

