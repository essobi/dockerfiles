FROM ubuntu:16.04  
MAINTAINER Shaun McCloud<git@smccloud.com>  
LABEL version="20171010"  
  
# Copy shell scripts  
ADD bootstrap.sh /  
ADD run.sh /  
ADD prerun.sh /  
  
# Run the bootstrap script  
RUN bash /bootstrap.sh  
  
# Stop the container  
STOPSIGNAL SIGTERM  
  
ENV WALLET_ADDRESS a  
ENV POOL_PASSWORD a  
ENV POOL pool.supportxmr.com:3333  
# Run the miner  
CMD ["bash", "/prerun.sh"]  

