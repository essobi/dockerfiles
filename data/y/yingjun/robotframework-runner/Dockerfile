FROM ubuntu:16.04  
MAINTAINER Ying <wandy1208@gmail.com>  
  
ENV ROOT_PASSWORD root  
  
RUN apt-get -qqy update \  
&& apt-get -qqy --no-install-recommends install \  
python2.7 \  
python-pip \  
python-lxml \  
bash \  
wget \  
curl \  
unzip \  
git  
  
RUN apt-get install -y python-wxgtk3.0  
  
#ssh-server  
RUN apt-get -qqy update \  
&& apt-get -qqy install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& echo "root:${ROOT_PASSWORD}" | chpasswd \  
&& sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
\  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
# Fixed python-wxgtk2.8 not available issue  
# Reference https://askubuntu.com/questions/789302/install-python-wxgtk2-8-on-
ubuntu-16-04  
# RUN echo "deb http://archive.ubuntu.com/ubuntu wily main universe" | tee
/etc/apt/sources.list.d/wily-copies.list \  
# apt-get install --reinstall -d `apt-cache depends python-wxgtk2.8 | grep
Depends | cut -d: f2 |tr -d "<>"`  
#########################################  
## REPOSITORIES AND DEPENDENCIES ##  
#########################################  
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe
restricted' > /etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main universe
restricted' >> /etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install -y python-wxgtk2.8 \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
RUN echo 'deb http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted
universe multiverse' > /etc/apt/sources.list && \  
echo 'deb http://cn.archive.ubuntu.com/ubuntu/ xenial-security main restricted
universe multiverse' >> /etc/apt/sources.list && \  
echo 'deb http://cn.archive.ubuntu.com/ubuntu/ xenial-updates main restricted
universe multiverse' >> /etc/apt/sources.list && \  
echo 'deb http://cn.archive.ubuntu.com/ubuntu/ xenial-backports main
restricted universe multiverse' >> /etc/apt/sources.list && \  
##測試版源  
echo 'deb http://cn.archive.ubuntu.com/ubuntu/ xenial-proposed main restricted
universe multiverse' >> /etc/apt/sources.list && \  
# 源碼  
echo 'deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted
universe multiverse' >> /etc/apt/sources.list && \  
echo 'deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-security main
restricted universe multiverse' >> /etc/apt/sources.list && \  
echo 'deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-updates main
restricted universe multiverse' >> /etc/apt/sources.list && \  
echo 'deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-backports main
restricted universe multiverse' >> /etc/apt/sources.list && \  
##測試版源  
echo 'deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-proposed main
restricted universe multiverse' >> /etc/apt/sources.list  
  
  
COPY scripts/ /home/seluser/exec/  
##Robot env  
# RUN pip install --upgrade pip \  
# &&  
RUN pip install --upgrade setuptools  
RUN pip install -Ur /home/seluser/exec/requirements.txt  
  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["entrypoint.sh"]

