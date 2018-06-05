FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get -y install python3 python3-pip  
RUN pip3 install requests progressbar2  
  
VOLUME /data  
  
WORKDIR /run  
  
COPY download_sections.py /run/  
RUN chmod +x /run/download_sections.py  
  
ENTRYPOINT ["/run/download_sections.py --datapath /data"]  

