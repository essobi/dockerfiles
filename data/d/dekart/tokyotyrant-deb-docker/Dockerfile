FROM debian:jessie  
MAINTAINER Dumitru  
  
LABEL description="Tokyo Tyrant custom image" version="0.0.1"  
EXPOSE 35871  
RUN mkdir /var/ttserver  
  
VOLUME /var/ttserver  
  
RUN apt-get update && apt-get install -y zlib1g-dev libbz2-dev  
  
ADD ["tokyocabinet_1.4.48-1_amd64.deb", "tokyotyrant_1.1.41-1_amd64.deb",
"/root/"]  
  
RUN dpkg -i /root/tokyocabinet_1.4.48-1_amd64.deb && \  
dpkg -i /root/tokyotyrant_1.1.41-1_amd64.deb  
  
  
ENTRYPOINT ["ttserver"]  
CMD ["-help"]  

