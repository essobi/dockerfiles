FROM debian:latest  
  
# install dependencies and go-server  
RUN apt-get update \  
&& apt-get install -y \  
lua5.1 luarocks \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN luarocks install busted  
  
VOLUME ["/host"]  
WORKDIR /host  
ENTRYPOINT ["busted"]  

