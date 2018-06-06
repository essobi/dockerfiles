FROM ubuntu:14.04.4  
MAINTAINER wention xuyi.828@gmail.com  
  
#ENV MIRROR mirrors.163.com  
ENV SERVER 0.0.0.0  
ENV ROOT_PASSWORD 123456  
# change the default mirrors  
#RUN sed -i 's/archive.ubuntu.com/mirrors.163.com/' /etc/apt/sources.list  
# update mirrors  
RUN apt-get update  
  
RUN apt-get install -y git make python debhelper python-cheetah \  
python-yaml git-core apache2 libapache2-mod-python libapache2-mod-wsgi \  
python-support python-netaddr python-simplejson python-urlgrabber \  
python-django debmirror syslinux wget rsync curl genisoimage \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
#COPY cobbler/ /root/cobbler/  
RUN git clone https://github.com/cobbler/cobbler.git  
  
RUN cd /root/cobbler && git checkout v2.6.11 \  
&&make install  
  
RUN ln -s /usr/local/lib/python2.7/dist-packages/cobbler
/usr/lib/python2.7/dist-packages/  
RUN a2enconf cobbler_web.conf cobbler.conf  
RUN a2enmod proxy_http  
  
RUN PASSWORD=`openssl passwd -1 -salt hLGoLIZR $ROOT_PASSWORD` \  
&& sed -i "s#^default_password.*#default_password_crypted: \"$PASSWORD\"#g"
/etc/cobbler/settings  
RUN sed -i "s/^server: 127.0.0.1/server: $SERVER/g" /etc/cobbler/settings \  
&& sed -i "s/^next_server: 127.0.0.1/next_server: $SERVER/g"
/etc/cobbler/settings  
  
RUN grep --color=auto -n "^default_password" /etc/cobbler/settings  
RUN grep --color=auto -n "^server:" /etc/cobbler/settings  
  
RUN mkdir /tftpboot  
  
RUN service apache2 restart \  
&& service cobblerd restart \  
&& cobbler get-loaders \  
&& cobbler check \  
&& cobbler sync  
  
CMD ['bash']  
  
VOLUME ["/mnt"]  
  
EXPOSE 25151  
EXPOSE 67/udp  
EXPOSE 69/udp  
EXPOSE 80  
EXPOSE 443  

