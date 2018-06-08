FROM selenium/standalone-chrome  
  
RUN sudo apt-get -y update && sudo apt-get install -y openssh-server  
  
USER root  
  
RUN echo "root:root" | chpasswd \  
&& sed -i '/PermitRootLogin prohibit-password/c\PermitRootLogin yes'
/etc/ssh/sshd_config  
  
COPY entry_point.sh /opt/bin/entry_point.sh  
  
RUN chmod +x /opt/bin/entry_point.sh  
  
ENTRYPOINT /opt/bin/entry_point.sh  
  
EXPOSE 22

