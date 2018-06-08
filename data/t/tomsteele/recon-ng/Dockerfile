FROM python:2.7.9  
MAINTAINER Tom Steele <tom@stacktitan.com>  
  
WORKDIR /root  
RUN git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/recon-ng.git  
WORKDIR /root/recon-ng  
RUN pip install -r REQUIREMENTS  
  
CMD ["./recon-ng"]  

