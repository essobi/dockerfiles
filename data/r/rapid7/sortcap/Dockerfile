FROM alpine:3.2  
RUN apk add --update python python-dev py-pip wireshark-common  
RUN pip install dpkt prettytable  
  
ADD sortcap /opt/sortcap  
ADD searchcap /opt/searchcap  
ADD pcaptools.py /opt/pcaptools.py  
  
WORKDIR /pcap  
ENTRYPOINT ["/opt/sortcap"]  
  
# Clean up APT when done.  
RUN rm -rf /var/cache/apk/*  

