FROM debian:wheezy  
MAINTAINER Paul Smith code@uvwxy.de  
  
# dependency setup  
RUN echo "nagios3-cgi nagios3/adminpassword string admin" | debconf-set-
selections  
RUN echo "nagios3-cgi nagios3/adminpassword-repeat string admin" | debconf-
set-selections  
RUN apt-get update  
RUN apt-get install -y \  
check-mk-livestatus \  
build-essential \  
libapache2-mod-python \  
nagios3 \  
python \  
sudo  
RUN apt-get clean  
  
ENV CMK_VERSION 1.2.4p5  
ENV CMK_FILE check_mk-$CMK_VERSION.tar.gz  
  
# fix check_mk looking in wrong places  
RUN cd /etc/ && ln -s nagios3 nagios  
RUN cd /usr/sbin/ && ln -s nagios3 nagios  
RUN cd /var/lib/ && rmdir nagios && ln -s nagios3 nagios  
RUN cd /var/log/ && ln -s /var/lib/nagios3 nagios  
RUN cd /etc/init.d/ && ln -s nagios3 nagios  
  
# add default admin account  
RUN cd /etc/nagios/ && htpasswd -bc htpasswd.users admin admin  
  
# add sudo rules required for check_mk  
RUN echo "Defaults:www-data !requiretty" >> /etc/sudoers  
RUN echo "nagios ALL = (root) NOPASSWD: /usr/bin/check_mk --automation *" >>
/etc/sudoers  
  
# register livestatus  
RUN echo "broker_module=/usr/lib/check_mk/livestatus.o
/var/lib/nagios/rw/live" >> /etc/nagios3/nagios.cfg  
RUN echo "event_broker_options=-1" >> /etc/nagios3/nagios.cfg  
  
# checkmk installation  
ADD http://mathias-kettner.de/download/$CMK_FILE /setup/  
RUN cd /setup/ && tar -xf check_mk-$CMK_VERSION.tar.gz  
RUN cd /setup/check_mk-$CMK_VERSION/ && bash setup.sh --yes  
  
# fix check_mk config (again)  
RUN sed -e 's/\/var\/log\/nagios\/rw\/live/\/var\/lib\/nagios3\/rw\/live/g' -i
/usr/share/check_mk/web/htdocs/defaults.py  
RUN sed -e 's/nagiosadmin/admin/g' -i /etc/check_mk/multisite.mk  
  
RUN chown nagios /etc/nagios/htpasswd.users  
RUN chown nagios /etc/nagios/auth.serials  
  
RUN cd /var/lib/check_mk/wato && mkdir auth && chgrp nagios auth && chmod 770
auth/  
#RUN usermod -a -G nagios www-data  
RUN rm -rf /setup/*  
  
ADD run.sh /  
CMD ["bash", "/run.sh"]  

