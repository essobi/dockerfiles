FROM debian:jessie  
MAINTAINER Stephane Bres "stephanejrbres@gmail.com"  
ADD http://www.mersenne.org/ftp_root/gimps/p95v293.linux64.tar.gz gimps.tar.gz  
RUN mkdir -p /gimps  
RUN tar -zxvf gimps.tar.gz -C /gimps  
ENTRYPOINT /gimps/mprime  
  
# docker build -t gimps_mprime .  
# docker run -it gimps_mprime  

