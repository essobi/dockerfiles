FROM kalilinux/kali-linux-docker  
  
  
## Install an SSH of your choice.  
ADD key.pub /tmp/your_key.pub  
RUN mkdir /root/.ssh && cat /tmp/your_key.pub >> /root/.ssh/authorized_keys &&
rm -f /tmp/your_key.pub && apt install -y openssh-server && apt clean  
  
RUN service ssh start  

