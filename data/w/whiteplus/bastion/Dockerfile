FROM debian:jessie  
  
MAINTAINER WHITEPLUS System "sysadmin@wh-plus.com"  
  
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& apt-get update 1> /dev/null \  
&& apt-get upgrade -y -q --no-install-recommends 1> /dev/null \  
&& apt-get install -y \--no-install-recommends \  
python \  
curl \  
openssh-server \  
mysql-client \  
squid3 \  
supervisor \  
1> /dev/null \  
&& apt-get clean 1> /dev/null \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
1> /dev/null \  
&& pip install redis 1> /dev/null \  
&& pip install Flask 1> /dev/null  
  
COPY files /tmp/files  
  
RUN mkdir /var/run/sshd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin no/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& mkdir -p /root/.ssh \  
&& chmod 700 /root/.ssh \  
&& touch /var/run/bastion.default.authkeys \  
&& chmod 600 /var/run/bastion.default.authkeys \  
&& ln -fns /var/run/bastion.default.authkeys /root/.ssh/authorized_keys \  
&& cp /tmp/files/supervisord.conf /etc/supervisor \  
&& cp /tmp/files/api-server.py /var/run \  
&& cp /etc/squid3/squid.conf /root/ \  
&& cp /tmp/files/squid.conf /etc/squid3/ \  
&& chown root:root /var/spool/squid3 \  
&& rm -rf /tmp/files  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 80 22 3128  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

