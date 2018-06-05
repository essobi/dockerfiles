From docker.elastic.co/beats/packetbeat:5.6.1  
  
USER root  
COPY tools /usr/share/packetbeat/  
RUN chmod +x /usr/share/packetbeat/tools  
ENV BUFFERSIZE=5 INTERVAL=2s TABLE=PacketBeat DEBUG=false  
CMD ["/bin/sh", "-c", "/usr/share/packetbeat/packetbeat -e -c
/etc/packetbeat/packetbeat.yml | ./tools -bufferSize=$BUFFERSIZE
-interval=$INTERVAL -table=$TABLE -debug=$DEBUG"]

