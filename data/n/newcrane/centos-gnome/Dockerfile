FROM centos:centos6  
MAINTAINER Crane <crane001@163.com>  
  
ENV ROOT_PASSWD=centospassword  
  
# Install base( except "X Window System" "fonts" )  
RUN yum update -y && yum groupinstall -y \  
"Desktop" \  
&& yum install -y \  
epel-release \  
sudo \  
gedit \  
python-setuptools \  
&& yum clean all && rm -rf /tmp/*  
  
# Supervisor  
RUN easy_install supervisor \  
&& mkdir -p /var/log/supervisor \  
&& mkdir -p /etc/supervisord.d \  
&& { \  
echo '[supervisord]'; \  
echo 'nodaemon=true'; \  
echo 'logfile=/var/log/supervisor/supervisord.log'; \  
echo 'logfile_maxbytes=10MB'; \  
echo 'logfile_backups=2'; \  
echo 'loglevel=warn'; \  
echo 'pidfile=/var/run/supervisord.pid'; \  
echo '[include]'; \  
echo 'files = /etc/supervisord.d/*.conf'; \  
} > /etc/supervisord.conf  
  
# VNC & XRDP Servers & Autostart services  
# tigervnc, tigervnc-server, tigervnc-server-module, xrdp, xinitd  
RUN yum update -y \  
&& yum install -y \  
tigervnc-server \  
xrdp \  
xinetd \  
&& yum clean all && rm -rf /tmp/* \  
&& chkconfig vncserver on 3456 \  
&& { \  
echo 'VNCSERVERS="0:root"'; \  
echo 'VNCSERVERARGS[0]="-geometry 1024x768"'; \  
} >> /etc/sysconfig/vncservers \  
&& chkconfig xrdp on 3456 \  
&& chmod -v +x /etc/init.d/xrdp \  
&& chmod -v +x /etc/xrdp/startwm.sh \  
&& echo "gnome-session --session=gnome" > ~/.xsession \  
&& { \  
echo '[program:xrdp]'; \  
echo 'command=/etc/init.d/xrdp restart'; \  
echo 'stderr_logfile=/var/log/supervisor/xrdp-error.log'; \  
echo 'stdout_logfile=/var/log/supervisor/xrdp.log'; \  
} > /etc/supervisord.d/xrdp.conf \  
&& { \  
echo '[program:vncserver]'; \  
echo 'command=/etc/init.d/vncserver restart'; \  
echo 'stderr_logfile=/var/log/supervisor/vncserver-error.log'; \  
echo 'stdout_logfile=/var/log/supervisor/vncserver.log'; \  
} > /etc/supervisord.d/vnc.conf  
  
# Create User  
RUN su root sh -c "yes $ROOT_PASSWD | vncpasswd" \  
&& echo "root:$ROOT_PASSWD" | chpasswd  
# time zone  
RUN sed -i -e "s:ZONE=\"Etc/UTC\":ZONE=\"Asia/Shanghai\":"
/etc/sysconfig/clock \  
&& rm -rf /etc/localtime \  
&& cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
  
EXPOSE 5900 3389  
# COPY docker-entrypoint.sh /entrypoint.sh  
# ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["supervisord"]  

