FROM phusion/baseimage:0.9.19  
ENV HOME /root  
  
RUN apt-get update -y  
RUN apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y mysql-server-5.7 zip
python nodejs npm python-pip  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

