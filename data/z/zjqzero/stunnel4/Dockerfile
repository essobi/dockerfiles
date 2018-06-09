FROM ubuntu:14.04  
# So that we can run as unprivileged user inside the container.  
RUN apt-get update && apt-get install -y stunnel4 && rm -rf
/var/lib/apt/lists/*  
  
ADD stunnel.conf /etc/stunnel/stunnel.conf  
ADD server.pem /etc/stunnel/server.pem  
  
RUN sed -i s/ENABLED=0/ENABLED=1/ /etc/default/stunnel4  
  
EXPOSE 5000  
# The following flags have to be specified when starting this container:  
# -network  
# Refer to -help for documentation on them.  
CMD ["/usr/bin/stunnel4", "/etc/stunnel/stunnel.conf"]  

