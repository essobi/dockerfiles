From ds82/ubuntu-i386:8.04  
  
MAINTAINER Robert Grzelka <robert.grzelka@outlook.com>  
  
  
################################################################################  
####INFO : this file is meant to build remotely  
################################################################################  
  
  
WORKDIR /  
  
RUN apt-get install -y \  
wget gcc-3.4-base gcc-3.4 g++-3.4 gdb \  
libncursesw5 libncurses5-dev libexpat1-dev \  
make xorg-dev gcc-4.2 libglib2.0-dev \  
openssh-server cmake gcc build-essential \  
vim python tcpdump telnet byacc flex iproute\  
gdb less bison valgrind firefox  
  
RUN apt-get clean  
  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-3.4 20 \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.2 10 \  
&& update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-3.4 20  
  
  
  
################################################################################  
####ssh SETTINGS  
################################################################################  
  
RUN mkdir -p /var/run/sshd ; chmod -rx /var/run/sshd  
RUN echo 'root:root' | chpasswd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -y  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN /etc/init.d/ssh start  
  
  
EXPOSE 22 9595 7575 1234  
  
################################################################################  
#### PINTOS SETTINGS  
################################################################################  
  
  
#write env variables  
ENV setup_dir /pintos/setup  
ENV pintos_dir /pintos  
ENV pintos_src /pintos/pintos/src  
  
#create volume that will appear at runtime mounted  
VOLUME [$pintos_dir]  
  
RUN mkdir -p $pintos_dir  
RUN mkdir -p $setup_dir  
RUN mkdir -p $pintos_src  
  
WORKDIR $setup_dir  
  
ADD setup $setup_dir  
ADD pintos $pintos_dir/pintos  
ADD pintos-misc $pintos_src/misc/  
ADD pintos-utils $pintos_dir/pintos-utils/  
  
RUN cp -r $pintos_dir/pintos-utils/* $pintos_src/utils/  
  
RUN ls -la $pintos_dir  
RUN ls -la $setup_dir  
  
RUN chmod -R 777 $pintos_dir  
  
RUN env SRCDIR=$setup_dir \  
PINTOSDIR=$pintos_dir/pintos/ \  
DSTDIR=/usr/local/ \  
/bin/bash $pintos_src/misc/bochs-2.2.6-build.sh  
  
#RUN rpm -i $setup_dir/qemu-img-0.15.0-1.el6.rfx.x86_64.rpm  
#RUN rpm -i $setup_dir/qemu-0.15.0-1.el6.rfx.x86_64.rpm  
  
  
  
RUN update-alternatives --set gcc /usr/bin/gcc-4.2  
  
RUN cd $setup_dir && tar xzf qemu-0.15.0.tar.gz && \  
cd qemu-0.15.0 && ./configure --target-list=i386-softmmu \  
&& make install  
  
RUN update-alternatives --set gcc /usr/bin/gcc-3.4  
  
USER root  
WORKDIR /root  
  
#this is only temporary variable  
env PATH $pintos_src/utils/:$PATH  
  
RUN echo export PATH=$PATH:$pintos_src/utils >> .profile  
RUN echo export PATH=$PATH:$pintos_src/utils >> .bashrc  
  
WORKDIR $pintos_src/utils/  
  
RUN make  
  
WORKDIR /pintos  
  
CMD ["/usr/sbin/sshd", "-D"]  
  
## to run (powershell admin):  
# ipconfig (get IPv4 Address)  
# set-variable -name DISPLAY -value 192.168.1.103:0.0  
## create junction of "pintos"  
## ...at "E:\EDA093 - Operating Systems\EDA093_CODE\pintos"  
## ...to "E:\Docker-Containers\docker-pintos\pintos"  
## so that we will work in second dir that files links to first one  
# cd "E:\Docker-Containers\docker-pintos"  
# docker run -itd -p 3522:22 -p 7575:7575 -p 9595:9595 -p 1234:1234 -h
localhost --privileged --security-opt seccomp:unconfined -e DISPLAY=$DISPLAY
--name pintos-container --dns=8.8.8.8 -v $PWD\pintos\src:/pintos/pintos/src -P
pintos-docker  
  
## to restart  
#docker ps -a  
#docker start -t "id"  
  
## to ssh  
#ssh -X -p 3522 root@127.0.0.1  
  
## to open gui (ie. firefox) from ssh with display on host  
#on host: run "XLaunch" > Multiple Windows > .. no cli.. > addit...: -ac >
Finish  
#on ssh: export DISPLAY=192.168.1.103:0.0 && firefox

