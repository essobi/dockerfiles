FROM ubuntu:14.04  
ADD p1.sh /var/p1.sh  
RUN chmod +x /var/p1.sh  
RUN /var/p1.sh  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nano  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

