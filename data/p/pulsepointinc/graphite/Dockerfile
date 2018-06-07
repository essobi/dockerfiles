FROM centos:7  
  
CMD ["/start.sh"]  
  
RUN \  
yum install -y epel-release && \  
yum install -y \  
gcc \  
pycairo \  
python-devel \  
python-django-tagging \  
python-gunicorn \  
python-pip \  
pytz \  
supervisor && \  
yum clean all  
  
ENV GRAPHITE_VERSION=0.9.15  
  
RUN \  
pip install "Twisted>=11,<12" && \  
pip install "whisper==${GRAPHITE_VERSION}" && \  
pip install --install-option="--prefix=/var/lib/graphite" \--install-option="
--install-lib=/var/lib/graphite/lib" "carbon==${GRAPHITE_VERSION}" && \  
pip install --install-option="--prefix=/var/lib/graphite" \--install-option="
--install-lib=/var/lib/graphite/webapp" "graphite-web==${GRAPHITE_VERSION}" &&
\  
rm -fr /root/.cache  
  
RUN \  
mv /var/lib/graphite/conf/carbon.conf.example
/var/lib/graphite/conf/carbon.conf && \  
mv /var/lib/graphite/conf/storage-schemas.conf.example
/var/lib/graphite/conf/storage-schemas.conf && \  
mv /var/lib/graphite/webapp/graphite/local_settings.py.example
/var/lib/graphite/webapp/graphite/local_settings.py && \  
cd /var/lib/graphite/webapp/graphite && \  
python manage.py syncdb --noinput  
  
COPY files/var/lib/graphite/conf/storage-aggregation.conf
/var/lib/graphite/conf/storage-aggregation.conf  
  
COPY files/etc/supervisord.conf /etc/supervisord.conf  
  
COPY files/start.sh /start.sh  
  
VOLUME ["/var/lib/graphite/storage", "/var/log"]  

