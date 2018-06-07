FROM ubuntu:trusty  
  
MAINTAINER Denis Trifonov <destrifonov@gmail.com>  
  
# install packages  
RUN apt-get update && apt-get install -y \  
git ca-certificates \  
supervisor \  
nginx \  
uwsgi uwsgi-plugin-python \  
python-pip \  
python-django \  
python-cairo \  
python-pyparsing \  
python-django-tagging \  
python-memcache \  
\--no-install-recommends && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install pytz  
  
# pulling applications  
WORKDIR /tmp  
RUN git clone https://github.com/graphite-project/graphite-web.git  
RUN git clone https://github.com/graphite-project/ceres.git  
RUN git clone https://github.com/graphite-project/whisper.git  
  
# install ceres database  
WORKDIR /tmp/ceres  
RUN git checkout master  
RUN python setup.py install  
  
# install whisper database  
WORKDIR /tmp/whisper  
RUN git checkout master  
RUN python setup.py install  
  
# install graphite web application  
WORKDIR /tmp/graphite-web  
RUN git checkout master  
RUN python setup.py install  
  
# clean up  
RUN rm -rf /tmp/* /var/tmp/* /etc/nginx/sites-available/* /etc/nginx/sites-
enabled/*  
  
# configure graphite-web  
RUN mkdir /opt/graphite/conf/webapp  
RUN cp /opt/graphite/webapp/graphite/local_settings.py.example
/opt/graphite/conf/webapp/local_settings.py  
RUN ln -s /opt/graphite/conf/webapp/local_settings.py
/opt/graphite/webapp/graphite/local_settings.py  
  
RUN cp /opt/graphite/conf/graphite.wsgi.example
/opt/graphite/conf/graphite.wsgi  
  
RUN PYTHONPATH="/opt/graphite/webapp" django-admin syncdb
--settings=graphite.settings --noinput  
  
RUN chown www-data -R /opt/graphite/storage  
  
# configure uwsgi  
ADD conf/graphite.ini /etc/uwsgi/apps-available/  
RUN ln -s /etc/uwsgi/apps-available/graphite.ini /etc/uwsgi/apps-
enabled/graphite.ini  
  
# configure nginx  
ADD conf/graphite.conf /etc/nginx/conf.d/graphite.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# configure supervisord  
ADD conf/supervisord.conf /etc/supervisor/conf.d/  
  
# define volume for override nginx configuration  
VOLUME /etc/nginx/conf.d  
# define volume for override graphite-web configuration  
VOLUME /opt/graphite/conf/webapp  
  
# expose nginx port  
EXPOSE 80  
# define default command on start container  
WORKDIR /usr/bin  
CMD ["supervisord"]

