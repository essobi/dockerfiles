FROM debian:latest  
  
MAINTAINER softsam  
  
RUN apt-get update && \  
apt-get -y install python-pip python-dev && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install vnc2flv==20100207 && \  
apt-get -y remove python-dev && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /tmp/* /var/tmp/*  
  
ENTRYPOINT ["flvrec.py"]  
CMD ["--help"]

