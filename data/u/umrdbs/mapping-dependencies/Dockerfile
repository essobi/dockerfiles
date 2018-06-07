# Ubuntu 16.04 LTS with Baseimage and Runit  
FROM phusion/baseimage:0.10.0  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Update the OS  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Setup directories  
WORKDIR /app  
COPY scripts /app/install  
  
RUN DEBIAN_FRONTEND=noninteractive chmod +x install/install-opencl.sh  
RUN DEBIAN_FRONTEND=noninteractive install/install-opencl.sh  
  
# ADD mapping-core /app/mapping-core  
#ADD mapping.conf /etc/mapping.conf  
RUN DEBIAN_FRONTEND=noninteractive chmod +x install/mapping-dependencies.sh  
RUN DEBIAN_FRONTEND=noninteractive install/mapping-dependencies.sh  
  
# Mount points for data folders  
VOLUME ["/app/rastersources"]  
  
# Remove install scripts  
RUN rm -rf /app/install  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Make port 80 available to the world outside this container  
EXPOSE 80  

