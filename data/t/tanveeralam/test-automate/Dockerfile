FROM tanveeralam/get-started:php  
  
MAINTAINER tanveeralam <tanveeralam1008@gmail.com>  
  
# disable interactive functionss  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set the working directory to /app  
WORKDIR /var/www/html/pos  
  
# Copy the current directory contents into the container at /app  
ADD . /var/www/html/pos  
  
RUN mkdir -p /var/pos/log \  
&& chmod -R 777 /var/pos/log \  
&& chmod -R 777 /var/www/html/pos  
  
# Expose apache.  
EXPOSE 80  

