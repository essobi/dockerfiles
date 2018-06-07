FROM ubuntu  
MAINTAINER Stefan Schoeffmann <stefan.schoeffmann@posteo.de>  
  
ENV LAST_UPDATE 2016-10-16  
RUN apt-get update && \  
apt-get install -y git curl vim less && \  
git clone https://github.com/lukas2511/dehydrated.git  
  
WORKDIR /dehydrated  
  
ENTRYPOINT ["./dehydrated"]  
CMD ['-h']  

