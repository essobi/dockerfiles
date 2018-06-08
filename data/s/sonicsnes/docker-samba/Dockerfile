FROM ubuntu:16.04  
  
RUN apt-get update && apt-get install -y \  
samba winbind \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD samba -i -s /var/lib/samba/private/smb.conf  

