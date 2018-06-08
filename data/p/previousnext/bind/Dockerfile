FROM previousnext/base  
MAINTAINER Nick Schuch "nick@previousnext.com.au"  
##  
# Bind.  
##  
# Install.  
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y bind9  
  
# Conf.  
ADD ./conf/bind/named.conf.options /etc/bind/named.conf.options  
ADD ./conf/bind/named.conf.local /etc/bind/named.conf.local  
ADD ./conf/bind/db.dev /etc/bind/db.dev  
  
##  
# Supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
EXPOSE 53  
CMD ["/root/start.sh"]  

