# start with a base image  
FROM ubuntu:15.04  
MAINTAINER DentalEMR <bradleybossard@dentalemr.com>  
  
# install dependencies  
RUN apt-get -y update  
  
RUN apt-get install -y wget \  
nginx \  
git \  
supervisor \  
# python dev dependencies  
python-pip \  
python-dev \  
postgresql \  
postgresql-contrib \  
libpq-dev \  
# for python pillow  
libjpeg-dev \  
# frontend dependencies  
nodejs \  
nodejs-legacy \  
npm \  
# for sass  
ruby \  
# for phantom  
libfontconfig  
  
RUN gem install sass  
  
RUN npm install --global gulp \  
bower \  
phantomjs  
  
USER postgres  
RUN /etc/init.d/postgresql start \  
&& psql --command "CREATE USER dentalemr_django WITH SUPERUSER PASSWORD
'1Ak5RTQt7mtw0OREsfPhJYzXIak41gnrm5NWYEosCeIduJck10awIzoys1wvbL8';" \  
&& createdb -O dentalemr_django dentalemr  
  
USER root  
  
# update working directories  
ADD ./config /config  
#ADD ./python_requirements /python_requirements  
# setup config  
#RUN pip install -r /python_requirements/requirements.txt  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN rm /etc/nginx/sites-available/default  
RUN ln -s /config/nginx.conf /etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
RUN ln -s /config/supervisor.conf /etc/supervisor/conf.d/  
  
ENV EMAIL_USER=dentaledr  
ENV EMAIL_PSWD=ZqAqwEIfY1KW69S9kyhM  
  
ENV DJANGO_SETTINGS_MODULE=core.settings.docker  
ENV DENTALEMR_DB_PASSWORD
1Ak5RTQt7mtw0OREsfPhJYzXIak41gnrm5NWYEosCeIduJck10awIzoys1wvbL8  
  
EXPOSE 80  
EXPOSE 3011  
CMD ["supervisord", "-n"]  

