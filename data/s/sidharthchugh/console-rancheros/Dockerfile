FROM tatsushid/tinycore:6.1-x86_64  
RUN tce-load -wic bash.tcz  
RUN tce-load -wic git  
RUN rm -rf /etc/ssh/*key*  
COPY entry.sh /usr/sbin/  
COPY console.sh /usr/sbin/  
COPY update-ssh-keys /usr/bin/  
RUN echo 'RancherOS \\\n \l' > /etc/issue  
RUN sudo addgroup -g 1100 rancher && \  
sudo addgroup -g 1101 docker && \  
sudo addgroup -g 1103 sudo && \  
sudo adduser -u 1100 -G rancher -D -h /home/rancher -s /bin/bash rancher && \  
sudo sed -i 's/\\(^docker.*\\)/\1rancher/g' /etc/group && \  
sudo sed -i 's/\\(^sudo.*\\)/\1rancher/g' /etc/group && \  
echo "sudo ALL=(ALL) ALL" | sudo tee -a /etc/sudoers  
sudo sed -i 's/rancher:!/rancher:*/g' /etc/shadow && \  
echo "## allow password less for rancher user" | sudo tee -a /etc/sudoers && \  
echo "rancher ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers  
ENTRYPOINT ["/usr/sbin/entry.sh"]  
CMD ["/usr/sbin/console.sh"]  

