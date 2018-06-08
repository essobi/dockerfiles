FROM ubuntu:12.04  
MAINTAINER Sunchan Lee <sunchanlee@inslab.co.kr>  
  
# make sure the package repository is up to date  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
# install sshd and supervisor  
RUN apt-get install -y openssh-server supervisor  
# install base dependencies  
RUN apt-get install -y python-setuptools python-dev patch subversion python-
svn git-core sqlite3 libsqlite3-dev python-ldap  
  
RUN easy_install pip  
  
# install reviewboard  
RUN pip install ReviewBoard  
  
# install supported DVCS  
RUN apt-get install -y python-subvertpy git-core  
  
# install external dependencies  
RUN apt-get install -y memcached python-memcache  
RUN apt-get install -y apache2 libapache2-mod-wsgi  
  
# initialize reviewboard  
RUN rb-site install --noinput --domain-name=reviews.local --site-
root=/reviewboard/ --db-type=sqlite3 --db-name=reviewboard --cache-
type=memcached --web-server-type=apache --admin-user=admin --admin-
password=admin --admin-email=noreply@inslab.co.kr /srv/reviews.local  
  
# update config with new data file location  
RUN sed -i 's/reviewboard/\/srv\/reviews.local\/data\/reviewboard/g'
/srv/reviews.local/conf/settings_local.py  
# turn debug on. Useful usually  
RUN sed -i 's/DEBUG = False/DEBUG = True/g'
/srv/reviews.local/conf/settings_local.py  
# recover SITE_ROOT  
RUN sed -i "s/^SITE_ROOT.*/SITE_ROOT = \'\/reviewboard\/\'/g"
/srv/reviews.local/conf/settings_local.py  
  
# fix permissions  
RUN chown -R www-data:www-data /srv/reviews.local/data
/srv/reviews.local/htdocs/media/uploaded /srv/reviews.local/htdocs/media/ext
/srv/reviews.local/data /srv/reviews.local/logs  
  
# configure apache  
RUN cp /srv/reviews.local/conf/apache-wsgi.conf /etc/apache2/sites-
available/reviews.local  
RUN a2dissite default  
RUN a2ensite reviews.local  
  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/run/apache2  
RUN mkdir -p /var/log/supervisor  
  
ADD supervisor/sshd.conf /etc/supervisor/conf.d/sshd.conf  
ADD supervisor/apache.conf /etc/supervisor/conf.d/apache.conf  
  
# add public key for passwordless auth  
ADD ssh_keys/id_rsa_docker.pub /tmp/id_rsa_docker.pub  
RUN mkdir -p /root/.ssh  
RUN cat /tmp/id_rsa_docker.pub >> /root/.ssh/authorized_keys  
  
#clean-up  
RUN rm /tmp/id_rsa_docker.pub  
RUN apt-get clean  
  
ADD scripts/run_supervisord.sh /usr/local/sbin/run_supervisord  
  
expose 22 80  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

