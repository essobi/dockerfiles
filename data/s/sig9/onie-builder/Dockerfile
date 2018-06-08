FROM debian:jessie  
  
MAINTAINER example@example.com  
  
RUN apt-get clean && apt-get update \  
&& apt-get install -y git-core sudo make wget pkg-config cpio \  
&& useradd -m builduser \  
&& echo 'builduser ALL=(ALL:ALL) ALL' >> /etc/sudoers \  
&& su builduser -c "cd /home/builduser/; git clone
https://github.com/opencomputeproject/onie" \  
&& cd /home/builduser/onie/build-config && make debian-prepare-build-host \  
&& su builduser -c "git config --global user.email example@example.com; git
config --global user.name example" \  
&& chsh -s /bin/bash builduser \  
&& echo 'export PATH=$PATH:/sbin/:/usr/sbin/' >> /home/builduser/.bashrc  

