FROM jamesjue/gabriel  
MAINTAINER Junjue Wang, junjuew@cs.cmu.edu  
  
WORKDIR /  
RUN git clone https://github.com/cmusatyalab/gabriel-lego.git  
  
EXPOSE 9098 9111  
CMD ["bash", "-c", "gabriel-control -n eth0 -l & sleep 5; gabriel-ucomm -s
127.0.0.1:8021 & sleep 5; cd /gabriel-lego && python proxy.py -s
127.0.0.1:8021"]

