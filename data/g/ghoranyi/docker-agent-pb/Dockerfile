FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libpcap0.8 curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV VERSION=1.2.3 PLATFORM=x86_64  
ENV FILENAME=packetbeat-${VERSION}-${PLATFORM}.tar.gz  
  
RUN curl -L -O -k https://download.elastic.co/beats/packetbeat/${FILENAME}\  
&& tar xzvf ${FILENAME}  
  
ADD packetbeat.logstash.yml /etc/packetbeat/packetbeat.logstash.yml  
ADD packetbeat.elastic.yml /etc/packetbeat/packetbeat.elastic.yml  
ADD start-pb.sh packetbeat-${VERSION}-${PLATFORM}/start-pb.sh  
WORKDIR packetbeat-${VERSION}-${PLATFORM}  
  
CMD ["./start-pb.sh"]  

