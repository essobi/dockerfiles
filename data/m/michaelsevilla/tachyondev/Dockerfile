FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
# install deps  
RUN echo "===> Installing jxio stuff..." && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \  
git openjdk-7-jdk curl \  
libtool autoconf automake build-essential \  
ibverbs-utils rdmacm-utils infiniband-diags perftest \  
librdmacm-dev libibverbs-dev numactl libnuma-dev libaio-dev libevent-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64/  
RUN echo "===> Build jxio..." && \  
cd / && \  
git clone https://github.com/accelio/JXIO.git && \  
cd /JXIO && \  
git clean -fd && \  
./build.sh  
  
# * modify sshd conf  
# * workaround for the way ubuntu deals with env for sudo  
# * add /ceph to PATH  
# * create expected dirs/links  
RUN sed -i "s/UsePAM.*/UsePAM yes/" /etc/ssh/sshd_config && \  
echo
"PATH=/ceph/src:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/ceph/bin"
>> /etc/environment && \  
echo "alias sudo='sudo env PATH=\$PATH'" >> /etc/environment && \  
sed -i "s/Defaults.*env_reset//" /etc/sudoers && \  
sed -i "s/Defaults.*secure_path.*//" /etc/sudoers  
  
# override tutum's run.sh with our own  
ADD run.sh /run.sh  

