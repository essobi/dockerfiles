FROM ubuntu:latest  
  
MAINTAINER Michael Lawrence <me@mikelawrence.co>  
  
VOLUME ["/starbound"]  
  
RUN apt-get update \  
&& apt-get install -y lib32gcc1 curl libpng12-0 \  
&& rm -rf /var/lib/apt/lists/*  
RUN mkdir -p /starbound /steamcmd \  
&& cd /steamcmd \  
&& curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | gunzip
-c | tar x  
  
COPY start.sh /start.sh  
  
EXPOSE 21025  
EXPOSE 21026  
CMD /start.sh  

