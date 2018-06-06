#FROM debian:wheezy  
FROM ubuntu:14.04  
MAINTAINER Jose Miguel de la Casa <nacicansao@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD sources.list /etc/apt/sources.list  
  
RUN echo "root:temporal" | chpasswd && \  
echo "deb http://http.debian.net/debian wheezy main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb http://http.debian.net/debian wheezy-updates main contrib non-free"
>> /etc/apt/sources.list && \  
echo "deb http://security.debian.org wheezy/updates main contrib non-free" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \--force-yes curl ssh supervisor apt-utils && \  
mkdir /var/run/sshd && \  
chown root:root /var/run/sshd && \  
mkdir /var/log/supervisord && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
apt-get -y \--force-yes install git python-pip gcc build-essential python-dev
wget tcpdump vim && \  
apt-get -y \--force-yes install virtualbox && \  
apt-get -y \--force-yes install python-magic python-dpkt python-mako \  
python-sqlalchemy python-jinja2 python-bottle ssdeep python-pyrex \  
subversion python-pymongo mongodb libcap2-bin  
  
RUN mkdir /home/workspace && \  
cd /home/workspace/ && \  
git clone git://github.com/cuckoobox/cuckoo.git && \  
pip install -r /home/workspace/cuckoo/requirements.txt && \  
useradd cuckoo && \  
usermod -a -G vboxusers cuckoo # add cuckoo to vboxusers group  
  
ADD start_cuckoo.sh /home/workspace/start_cuckoo.sh  
ADD start_cuckoo_web.sh /home/workspace/start_cuckoo_web.sh  
ADD virtualbox.conf /home/workspace/cuckoo/conf/virtualbox.conf  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# RUN setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump  
# RUN getcap /usr/sbin/tcpdump # to check changes have been applied  
  
EXPOSE 22 9001  
  
CMD ["/usr/bin/supervisord"]  

