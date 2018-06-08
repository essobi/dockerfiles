# Add JRE to the base ubuntu image  
FROM pallet/ubuntu-nodoc  
MAINTAINER Hugo Duncan <hugo@palletops.com>  
  
# Add JRE  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
openjdk-7-jre-headless  
RUN apt-get -y autoremove  
RUN apt-get -y autoclean  
RUN apt-get -y clean  

