FROM ubuntu:16.04  
MAINTAINER Oleksandr Kutsenko <olexander.kutsenko@gmail.com>  
  
# Update && Upgrade  
RUN apt-get update && apt-get upgrade -y  
  
# Install Dependencies  
RUN apt-get install -y software-properties-common python-software-properties \  
git git-core mc htop tmux sudo nano vim  
  
# Create AWS EC2 user  
RUN mkdir -p /home/ec2-user  
RUN useradd -d /home/ec2-user -s /bin/bash -M -N -G sudo,root ec2-user  
RUN echo ec2-user:ec2-user | chpasswd  
COPY configs/.bashrc /home/ec2-user/.bashrc  
COPY configs/.gitconfig /home/ec2-user  
RUN chown -R ec2-user /home/ec2-user  
  
# Install SSH service  
RUN apt-get install -y openssh-server openssh-client  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
#change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Copy configs bash autostart services  
COPY configs/autostart.sh /root/autostart.sh  
RUN chmod +x /root/autostart.sh  
COPY configs/bash.bashrc /etc/bash.bashrc  
COPY configs/.bashrc /root/.bashrc  
  
# Install locale  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Install password_storage  
RUN apt-get install pass -y  
  
# Set git global parameters for root user  
RUN git config --global user.email "root@your_company_domain.com"  
RUN git config --global user.name "Password Storage"  
  
#open ports  
EXPOSE 22  

