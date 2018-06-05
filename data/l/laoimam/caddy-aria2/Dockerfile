# version: 1  
FROM debian:jessie  
MAINTAINER laoimam "dockerhub@temp.tk"  
ENV BUILD_PATH /root/build  
RUN mkdir -p $BUILD_PATH  
WORKDIR $BUILD_PATH  
ADD https://raw.githubusercontent.com/zhzjwd/docker/master/debian-caddy-
aria2/sh/caddy_install.sh $BUILD_PATH/caddy_install.sh  
ADD https://raw.githubusercontent.com/zhzjwd/docker/master/debian-caddy-
aria2/sh/aria2.sh $BUILD_PATH/aria2.sh  
ADD https://raw.githubusercontent.com/zhzjwd/docker/master/debian-caddy-
aria2/sh/rclone.sh $BUILD_PATH/rclone.sh  
ADD https://raw.githubusercontent.com/zhzjwd/docker/master/debian-caddy-
aria2/sh/service_start.sh $BUILD_PATH/service_start.sh  
RUN apt-get update && \  
apt-get install -y openssh-server zip unzip unar screen curl wget sed git cron
locales locales-all iptables nano p7zip p7zip-full make fuse gcc g++ python
python-pip python3 python3-pip && \  
echo "deb http://packages.dotdeb.org jessie all\ndeb-src
http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list
&& \  
wget http://www.dotdeb.org/dotdeb.gpg -O /tmp/dotdeb.gpg && apt-key add
/tmp/dotdeb.gpg && rm /tmp/dotdeb.gpg && \  
apt-get update && \  
apt-get install -y php7.0 php7.0-fpm php7.0-cgi php7.0-curl php7.0-gd
php7.0-zip && \  
bash caddy_install.sh install http.filemanager,http.git && \  
bash aria2.sh install && \  
bash rclone.sh && \  
mkdir -p /var/run/sshd /var/run/php && \  
mkdir -p /home/down /home/ariang && \  
mkdir -p /root/.config/rclone /root/.aria2/cert && \  
mkdir -p /root/.ssh && touch /root/.ssh/authorized_keys && \  
chmod 755 /root/.ssh /root/.ssh/authorized_keys && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/^#PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
&& \  
sed -ri '/^PermitRootLogin/a\\#PermitRootLogin prohibit-password'
/etc/ssh/sshd_config && \  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# zh_HK.UTF-8 UTF-8/zh_HK.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# zh_TW.UTF-8 UTF-8/zh_TW.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# ko_KR.UTF-8 UTF-8/ko_KR.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen && localedef -i zh_CN -c -f UTF-8 zh_CN.UTF-8 && \  
update-locale LANG=zh_CN.UTF-8 && \  
echo "LC_ALL=zh_CN.UTF-8" >> /etc/default/locale && \  
echo "LANGUAGE=zh_CN.UTF-8" >> /etc/default/locale && \  
echo "export LC_ALL=zh_CN.UTF-8" >> /etc/profile && \  
echo "export LANG=zh_CN.UTF-8" >> /etc/profile && \  
echo
'PS1="\\[\e[36m\\][\\[\e[36m\\]\u\\[\e[0m\\]@\h\\[\e[35m\\]:\\[\e[32m\\]\w\\[\e[36m\\]]\\[\e[0m\\]\\\$"'
>> /root/.bashrc && \  
echo "debian" > /etc/hostname && \  
echo 'root:root' | chpasswd  
  
#ENV LC_ALL zh_CN.UTF-8  
#ENV LANG zh_CN.UTF-8  
  
EXPOSE 22  
  
CMD ["bash", "service_start.sh"]

