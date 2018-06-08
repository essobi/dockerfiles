FROM ubuntu:trusty  
MAINTAINER Wouter ten Bosch <woutertenbosch@gmail.com>  
  
# Install Nginx  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install nginx && \  
rm -rf /var/lib/apt/lists/*  
  
# Replace configuration  
RUN rm -v /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/  
  
# Add run script  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Set reverse proxy domain  
ENV REVERSE_DOMAIN example.com  
ENV REVERSE_PROTO http  
  
# Expose and start  
EXPOSE 80  
CMD ["/run.sh"]

