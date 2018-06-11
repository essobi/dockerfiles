FROM ubuntu:trusty  
MAINTAINER yp_ren@hotmail.com  
USER root  
  
RUN apt-get update \  
&& apt-get install -y \  
lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6 \  
build-essential ccache \  
libncurses5-dev libssl-dev \  
git subversion mercurial \  
gawk vim unzip \  
bash bash-completion \  
screen tmux wget \  
sudo openssh-server \  
&& apt-get autoremove \  
&& apt-get clean  
  
# 配置中文编码  
RUN locale-gen zh_CN.UTF-8 en_US.UTF-8 \  
&& echo 'LANG="zh_CN.UTF-8"' >> /etc/environment \  
&& echo 'LANGUAGE="en_US.UTF-8"' >> /etc/environment  
  
# 添加用户ubuntu  
RUN useradd -m -s /bin/bash ubuntu \  
&& echo 'ubuntu:ubuntu' | chpasswd \  
&& echo 'ubuntu ALL=NOPASSWD: ALL' > /etc/sudoers.d/ubuntu \  
&& chmod 440 /etc/sudoers.d/ubuntu  
  
# 配置ssh-server  
RUN mkdir /var/run/sshd \  
&& echo 'ClientAliveInterval 30' >> /etc/ssh/sshd_config \  
&& echo 'ClientAliveCountMax 6' >> /etc/ssh/sshd_config \  
&& sed -i 's/^Port 22$/Port 2022/g' /etc/ssh/sshd_config  
  
USER ubuntu  
WORKDIR /home/ubuntu  
  
CMD ["sudo","/usr/sbin/sshd","-D"]  

