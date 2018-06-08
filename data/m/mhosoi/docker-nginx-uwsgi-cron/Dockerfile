FROM centos:7  
MAINTAINER Masatsugu Hosoi<public.hosoi@gmail.com>  
  
# install nginx  
ADD etc/nginx.repo /etc/yum.repos.d/nginx.repo  
ADD etc/python_modules.txt /tmp/python_modules.txt  
  
RUN yum -y swap -- remove systemd-container systemd-container-libs -- install
systemd systemd-libs \  
&& yum -y install wget passwd cronie logrotate \  
openssh-server gcc python python-devel \  
python-setuptools nginx pyOpenSSL MySQL-python m2crypto zlib-devel \  
libmemcached-devel libmemcached python-crypto \  
&& easy_install pip \  
&& pip install supervisor==3.1.3 && pip install -r /tmp/python_modules.txt \  
&& mkdir -p /srv/dev/ \  
&& yum remove -y gcc cpp glibc-devel glibc-headers kernel-headers python-devel
libmemcached-devel zlib-devel \  
&& rm -rf /var/cache/* \  
&& mkdir -p /var/cache/nginx \  
&& localedef --list-archive | grep -v -e ^ja -e ^en_GB -e en_US -e ^zh | xargs
localedef --delete-from-archive \  
&& cp -a /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl \  
&& build-locale-archive \  
&& mkdir /tmp/locale \  
&& cp -R /usr/share/locale/en /usr/share/locale/en_US /tmp/locale \  
&& rm -rf /usr/share/locale/* \  
&& mv /tmp/locale/* /usr/share/locale/ \  
&& rmdir /tmp/locale \  
&& mkdir /tmp/locale \  
&& cp -R /usr/share/i18n/locales/en_US /tmp/locale \  
&& rm -rf /usr/share/i18n/locales/* \  
&& mv /tmp/locale/* /usr/share/i18n/locales/ \  
&& rmdir /tmp/locale \  
&& rm -rf /root/.cache \  
&& find /usr/lib/python2.7/site-packages/django/contrib/**/locale/* | grep -v
'/en/' | grep -v '/en$' | xargs rm -rf \  
&& find /usr/lib/python2.7/site-packages/django/conf/locale/* | grep -v '/en/'
| grep -v '/en$' | xargs rm -rf \  
&& yum clean all \  
&& rm -rf /var/log/*/* \  
&& rm -rf /var/cache/*/* \  
&& rm -rf /var/lib/yum \  
&& rm -rf /var/lib/rpm  
  
  
ADD etc/uwsgi.ini etc/supervisord.conf /etc/  
ADD etc/uwsgi_params etc/nginx.conf /etc/nginx/  
ADD etc/pam_crond /etc/pam.d/crond  
  
# ADD etc/cronjob /etc/cron.d/app  
# RUN chmod 644 /etc/cron.d/app  
# ADD app /srv/dev/server  
  
  
EXPOSE 80 22  
CMD ["/usr/bin/supervisord"]  

