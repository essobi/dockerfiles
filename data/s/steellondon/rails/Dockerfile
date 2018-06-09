FROM ruby:2.2.4  
MAINTAINER Giovanni Derks <giovanni.derks@steellondon.com>  
  
RUN apt-get update && \  
apt-get install -y build-essential libpq-dev && \  
apt-get install -y openssh-server libgmp3-dev && \  
apt-get install -y nodejs --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd && \  
echo 'root:root' | chpasswd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY app_setup /root/app_setup  
RUN chmod +x /root/app_setup/*.sh  
  
RUN gem update --system  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

