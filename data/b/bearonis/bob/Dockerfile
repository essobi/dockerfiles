FROM ubuntu:trusty  
  
RUN mkdir /data && \  
chmod 777 /data && \  
useradd -ms /bin/bash bob && \  
sed -i '/#force_color_prompt=yes/c\force_color_prompt=yes' /home/bob/.bashrc
&& \  
echo "bob ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers  
  
USER bob  
  
CMD /bin/bash  

