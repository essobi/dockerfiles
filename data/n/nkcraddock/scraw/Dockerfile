FROM phusion/baseimage  
  
ENV HOME /root  
  
# install all that good stuff  
RUN apt-get update && apt-get install -y \  
git \  
vim \  
curl \  
ruby1.9.1 \  
wget \  
mercurial \  
tmux \  
build-essential \  
silversearcher-ag && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install go  
RUN wget https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.4.2.linux-amd64.tar.gz && \  
mkdir -p ~/dev/go/src/github.com  
  
# Add homesick  
RUN gem install homesick gitignore  
  
# enable sshd  
RUN rm -rf /etc/service/sshd/down  
  
# enable the insecure key (dont expose sshd outside your localhost)  
RUN /usr/sbin/enable_insecure_key  
  
# Use baseimage-docker's init process  
CMD ["/sbin/my_init"]  
  
# create user directory  
RUN mkdir -p /home/scraw/.ssh  
  
# Add scripts  
ADD .bash_local /home/scraw/  
ADD init_homesick /home/scraw/  
  
# add the scraw user. (password: scraw)  
RUN \  
useradd -p $(echo "scraw" | openssl passwd -1 -stdin) -g root -s /bin/bash
scraw && \  
adduser scraw sudo && \  
cp /root/.ssh/authorized_keys /home/scraw/.ssh && \  
chown scraw /home/scraw -R  
  

