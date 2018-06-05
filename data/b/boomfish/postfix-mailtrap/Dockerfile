FROM catatnight/postfix  
  
MAINTAINER Dennis Clark <boomfish@gmail.com>  
  
# Replace install.sh on base image  
COPY install.sh /opt/install.sh  
RUN chmod u+x /opt/install.sh  
  
EXPOSE 25  
# Configuration defaults  
# Name of local mail domain (there's no need to change this)  
ENV maildomain localhost  
  
# Username of mailbox on host to capture all emails  
ENV mailbox_username vagrant  
  
# Change to false if mailbox belongs to a system user such as root (not
recommended)  
ENV mailbox_user_create true  
  
# UID of mailbox to capture all emails (required if mailbox_create_user is
true)  
ENV mailbox_uid 1000  
# Subnets of networks we will accept mail from without authentication  
ENV mynetworks "127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128 172.16.0.0/12"  

