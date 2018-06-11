FROM debian:jessie  
  
MAINTAINER loic  
  
RUN apt-get update && apt-get install -y \  
wget \  
ntp \  
unzip \  
curl \  
openssh-server \  
supervisor \  
tar \  
sudo \  
htop \  
iftop \  
net-tools \  
python \  
ca-certificates \  
vim \  
git \  
locate \  
dos2unix \  
libpam-google-authenticator \  
dnsutils  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "root:root" | chpasswd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed -i 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' /etc/pam.d/sshd  
  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
RUN sed -i '2i auth required pam_google_authenticator.so' /etc/pam.d/sshd  
RUN sed -i 's/ChallengeResponseAuthentication
no/ChallengeResponseAuthentication yes/' /etc/ssh/sshd_config  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD bashrc /root/.bashrc  
ADD profile /root/.profile  
ADD google_authenticator /root/.google_authenticator_default  
ADD init.sh /root/init.sh  
RUN chmod +x /root/init.sh  
CMD ["/root/init.sh"]  
EXPOSE 22  

