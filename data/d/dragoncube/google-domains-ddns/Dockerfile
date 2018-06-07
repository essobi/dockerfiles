FROM phusion/baseimage:0.9.17  
MAINTAINER Kirill Uvaev <me@dragoncube.net>  
  
VOLUME ["/config"]  
  
# Add dynamic dns script  
ADD google-domains-ddns.sh /root/google-domains-ddns/google-domains-ddns.sh  
RUN chmod +x /root/google-domains-ddns/google-domains-ddns.sh  
  
# Create template config file  
ADD google-domains-ddns.conf /root/google-domains-ddns/google-domains-
ddns.conf  
  
CMD /root/google-domains-ddns/google-domains-ddns.sh  

