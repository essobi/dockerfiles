FROM centos:latest  
MAINTAINER Stephen Price <steeef@gmail.com>  
  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install required packages  
RUN yum -y install gcc python-devel pycairo pyOpenSSL python-memcached \  
bitmap bitmap-fonts python-pip python-django-tagging \  
python-sqlite2 python-rrdtool memcached python-simplejson python-gunicorn \  
supervisor openssh-server sudo nginx  
  
# Use pip to install graphite, carbon, and deps  
RUN pip-python install whisper  
RUN pip-python install Twisted==11.1.0  
RUN pip-python install --install-option="--prefix=/var/lib/graphite"
\--install-option="--install-lib=/var/lib/graphite/lib" carbon  
RUN pip-python install --install-option="--prefix=/var/lib/graphite"
\--install-option="--install-lib=/var/lib/graphite/webapp" graphite-web  
  
RUN mkdir -p /var/run/sshd  
RUN chmod -rx /var/run/sshd  
  
RUN useradd -d /home/graphite -m -s /bin/bash graphite  
RUN echo graphite:graphite | chpasswd  
RUN echo 'graphite ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/graphite  
RUN chmod 0440 /etc/sudoers.d/graphite  
  
# Add system service config  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisord.conf  
#  
## Add graphite config  
ADD initial_data.json /var/lib/graphite/webapp/graphite/initial_data.json  
ADD local_settings.py /var/lib/graphite/webapp/graphite/local_settings.py  
ADD carbon.conf /var/lib/graphite/conf/carbon.conf  
ADD storage-schemas.conf /var/lib/graphite/conf/storage-schemas.conf  
RUN mkdir -p /var/lib/graphite/storage/whisper  
RUN touch /var/lib/graphite/storage/graphite.db
/var/lib/graphite/storage/index  
RUN chown -R nginx /var/lib/graphite/storage  
RUN chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper  
RUN chmod 0664 /var/lib/graphite/storage/graphite.db  
RUN cd /var/lib/graphite/webapp/graphite && python manage.py syncdb \--noinput  
# Nginx  
EXPOSE 80  
# Carbon line receiver port  
EXPOSE 2003  
# Carbon pickle receiver port  
EXPOSE 2004  
# Carbon cache query port  
EXPOSE 7002  
# ssh  
EXPOSE 22  
  
ADD start.sh /tmp/start.sh  
RUN chmod +x /tmp/start.sh  
ENTRYPOINT /tmp/start.sh  

