FROM ubuntu:16.04  
# without this you will get errors like:  
# '...xenial_InReleaseCouldn't create tempfiles for splitting up /var/lib/...'  
# as well as erros similar to this, later down the line:  
# InRelease: Could not execute 'apt-key' to verify signature (is gnupg
installed?)  
RUN chown root:root /tmp && \  
chmod 1777 /tmp  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
  
RUN apt-get update -y  
RUN apt-get install -y sudo  
RUN apt-get install -y packagekit-gtk3-module  
RUN apt-get install -y libcanberra-gtk*  
RUN apt-get install -y chromium-browser  
RUN apt-get install -y xauth  
  
RUN apt-get autoremove &&\  
apt-get clean &&\  
rm -rf /tmp/*  
  

