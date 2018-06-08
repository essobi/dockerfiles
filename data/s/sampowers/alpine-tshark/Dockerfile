FROM alpine  
RUN apk add --no-cache tshark  
ENTRYPOINT ["dumpcap", "-P", "-w", "-", "-i", "eth0", "-"]  

