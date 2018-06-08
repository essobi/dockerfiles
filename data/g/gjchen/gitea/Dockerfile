FROM gjchen/alpine:3.7  
MAINTAINER gjchen <gjchen.tw@gmail.com>  
  
RUN apk --no-cache --no-progress upgrade -f && \  
apk --no-cache --no-progress add \  
su-exec \  
ca-certificates \  
sqlite \  
bash \  
git \  
linux-pam \  
s6 \  
curl \  
openssh \  
tzdata \  
gitea  
  
COPY s6.d /etc/s6.d  
COPY app.ini /etc/gitea/app.ini  
  
RUN ln -s /data/ssh/ssh_host_ed25519_key /etc/ssh/ && \  
ln -s /data/ssh/ssh_host_rsa_key /etc/ssh/ && \  
ln -s /data/ssh/ssh_host_dsa_key /etc/ssh && \  
ln -s /data/ssh/ssh_host_ecdsa_key /etc/ssh/  
  
ENV USER=git  
EXPOSE 3000 22  

