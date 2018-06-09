FROM tsutomu7/ubuntu-essential  
  
ENV USER=developer  
RUN export uid=1000 gid=1000 pswd=password && \  
apt-get update --fix-missing && \  
apt-get install -y --no-install-recommends sudo busybox && \  
/bin/busybox --install && \  
apt-get clean && \  
groupadd -g $gid $USER && \  
useradd -g $USER -G sudo -m -s /bin/bash $USER && \  
echo "$USER:$pswd" | chpasswd && \  
mkdir -p /home/$USER && \  
mkdir -p /etc/sudoers.d && \  
echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER && \  
chmod 0440 /etc/sudoers.d/$USER && \  
chown ${uid}:${gid} -R /home/$USER && \  
rm -rf /var/lib/apt/lists/*  
USER $USER  
ENV HOME /home/$USER  
CMD ["/bin/bash"]  

