# APN service definition  
#  
# To use, attach a data container with /etc/apn/cert.pem and /etc/apn/key.pem
files  
# and set the env var APN_HOST to the correct APN endpoint.  
#  
FROM busybox  
ADD apn /apn  
ADD start.sh /start.sh  
CMD ["/start.sh"]

