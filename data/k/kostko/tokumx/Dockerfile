FROM ubuntu:trusty  
MAINTAINER Jernej Kos, jernej@kos.mx  
  
# Expose MongoDB database port  
EXPOSE 27017  
# Add tokumx server source  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 505A7412  
RUN echo "deb [arch=amd64] http://s3.amazonaws.com/tokumx-debs $(lsb_release
-cs) main" > /etc/apt/sources.list.d/tokumx.list  
  
# Update packages  
RUN apt-get update  
  
# Install packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -y --force-
yes install tokumx  
  
# Install startup script  
ADD start.sh /meta/start.sh  
CMD ["/meta/start.sh"]  
  

