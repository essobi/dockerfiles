FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get install -y openssh-server git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& echo 'root:root' | chpasswd \  
&& echo "export VISIBLE=now" >> /etc/profile \  
&& mkdir /var/run/sshd \  
&& mkdir /app && mkdir /app.git && cd /app.git && git init --bare  
  
ADD post-receive /app.git/hooks/post-receive  
RUN chmod +x /app.git/hooks/post-receive  
  
EXPOSE 22  
WORKDIR /app.git  
CMD ["/usr/sbin/sshd", "-D"]  
  
# docker run --name git gallna/git  
# git remote add local ssh://root@git.docker/app.git  
# git push local  

