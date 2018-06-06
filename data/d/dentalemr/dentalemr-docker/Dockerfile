# start with a base image  
FROM ubuntu:14.04  
MAINTAINER DentalEMR <bradleybossard@dentalemr.com>  
  
# install dependencies  
RUN apt-get update  
RUN apt-get install -y wget \  
nginx \  
git \  
supervisor \  
# install backend python dev dependencies  
python-pip \  
python-dev \  
postgresql \  
postgresql-contrib \  
libpq-dev  
  
# install frontend dependencies  
RUN apt-get install -y nodejs \  
nodejs-legacy \  
npm \  
ruby  
RUN sudo gem install sass  
  
RUN npm install --global gulp  
RUN npm install --global bower  
  
ENV PHANTOMJS_VERSION 1.9.7  
RUN mkdir -p /srv/var  
RUN wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2  
  
RUN tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp  
RUN rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2  
RUN mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs  
RUN ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
USER postgres  
RUN /etc/init.d/postgresql start \  
&& psql --command "CREATE USER dentalemr_django WITH SUPERUSER PASSWORD
'1Ak5RTQt7mtw0OREsfPhJYzXIak41gnrm5NWYEosCeIduJck10awIzoys1wvbL8';" \  
&& createdb -O dentalemr_django dentalemr  
  
USER root  
  
# update working directories  
ADD ./config /config  
ADD ./python_requirements /python_requirements  
  
# setup config  
RUN pip install -r /python_requirements/requirements.txt  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN rm /etc/nginx/sites-available/default  
RUN ln -s /config/nginx.conf /etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
RUN ln -s /config/supervisor.conf /etc/supervisor/conf.d/  
  
#ENV DJANGO_SETTINGS_MODULE=core.settings.settings  
ENV DJANGO_SETTINGS_MODULE=core.settings.docker  
ENV DENTALEMR_DB_PASSWORD
1Ak5RTQt7mtw0OREsfPhJYzXIak41gnrm5NWYEosCeIduJck10awIzoys1wvbL8  
  
EXPOSE 80  
EXPOSE 3011  
CMD ["supervisord", "-n"]  

