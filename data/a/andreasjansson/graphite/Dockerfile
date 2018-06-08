FROM ubuntu:precise  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update  
RUN apt-get -y install \  
python-ldap \  
python-cairo \  
python-django \  
python-twisted \  
python-django-tagging \  
python-simplejson \  
python-memcache \  
python-pysqlite2 \  
python-support \  
python-pip \  
gunicorn \  
supervisor \  
nginx-light \  
openssh-server \  
apache2-utils  
  
RUN pip install whisper envtpl  
RUN pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/lib" carbon  
RUN pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/webapp" graphite-web  
  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD ./nginx.conf.tpl /etc/nginx/nginx.conf.tpl  
ADD ./local_settings.py /var/lib/graphite/webapp/graphite/local_settings.py  
ADD ./carbon.conf /var/lib/graphite/conf/carbon.conf  
ADD ./storage-schemas.conf /var/lib/graphite/conf/storage-schemas.conf  
RUN mkdir -p /var/lib/graphite/storage/whisper  
RUN touch /var/lib/graphite/storage/graphite.db
/var/lib/graphite/storage/index  
RUN chown -R www-data /var/lib/graphite/storage  
RUN chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper  
RUN chmod 0664 /var/lib/graphite/storage/graphite.db  
RUN cd /var/lib/graphite/webapp/graphite && python manage.py syncdb \--noinput  
  
RUN echo 'root:root' | chpasswd  
RUN mkdir /var/run/sshd  
  
ADD start_container /usr/bin/start_container  
RUN chmod 777 /usr/bin/start_container  
  
EXPOSE 22 80 2003 2004 7002  
  
CMD start_container  

