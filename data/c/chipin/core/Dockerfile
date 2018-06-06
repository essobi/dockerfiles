FROM centos:7  
MAINTAINER "Mitsuru Nakakawaji" <mitsuru@procube.jp>  
RUN yum -y update \  
&& yum -y install unzip wget sudo lsof telnet bind-utils tar tcpdump vim
sysstat strace less  
ENV HOME /root  
WORKDIR ${HOME}  
RUN echo "export TERM=xterm" >> .bash_profile  
RUN yum install -y epel-release httpd  
RUN yum install -y mosquitto certbot  
ENV NODEJS_VERSION=v8.5.0  
RUN wget -qO -
https://nodejs.org/dist/${NODEJS_VERSION}/node-${NODEJS_VERSION}-linux-x64.tar.xz
| tar xf - -C /usr/local -J \  
&& ln -s /usr/local/node-${NODEJS_VERSION}-linux-x64 /usr/local/nodejs  
RUN wget -qO - https://github.com/procube-open/shibboleth-fcgi-
rpm/releases/download/2.6.0-2.2-1/shibboleth-fcgi-rpm.tar.gz | tar -xzf -  
RUN wget -qO - https://github.com/procube-open/nginx-shib-
rpm/releases/download/1.12.1-1-1/nginx-shib-rpm.tar.gz | tar -xzf -  
RUN wget -qO - https://github.com/chip-
in/configure/releases/download/1.0.0-d1/configure-rpm.tar.gz | tar -xzf -  
RUN wget -qO - https://github.com/procube-open/jwt-nginx-
lua/releases/download/1.0.1/jwt-nginx-lua.tar.gz | tar -xzf -  
RUN wget -qO - https://github.com/chip-in/hmr/releases/download/0.0.7/hmr-
rpm.tar.gz | tar -xzf -  
RUN yum install -y RPMS/x86_64/*.rpm \  
&& mkdir /etc/systemd/system/nginx.service.d \  
&& printf "[Service]\nExecStartPost=/bin/sleep 0.1\n" >
/etc/systemd/system/nginx.service.d/override.conf  
RUN systemctl enable nginx mosquitto shibd shibfcgi hmr \  
jwtIssuer-config jwtVerifier-config renewCerts.timer shibboleth-config load-
certificates  
RUN echo -e "port 1833\nprotocol websockets" >> /etc/mosquitto/mosquitto.conf  
RUN touch /etc/sysconfig/network  
ENV container docker  
STOPSIGNAL 37  
EXPOSE 80  
EXPOSE 443  
CMD ["/sbin/init"]  

