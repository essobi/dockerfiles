FROM progtologist/ruby  
MAINTAINER Aris Synodinos <arissynod@gmail.com>  
  
# Set up application user 'openproject' and check out source  
RUN adduser openproject --home /home/openproject --shell /bin/bash --disabled-
password --gecos "" &&\  
mkdir -p /var/www/openproject &&\  
git clone https://github.com/opf/openproject.git -b v5.0.19 --single-branch
/var/www/openproject &&\  
mkdir -p /var/www/openproject/docker/scripts  
  
COPY Gemfile.local /var/www/openproject/  
COPY Gemfile.plugins /var/www/openproject/  
  
RUN chown -R openproject:openproject /var/www/openproject  
  
USER openproject  
  
RUN cd /var/www/openproject &&\  
bundle install --without mysql mysql2 sqlite development test rmagick --path
vendor/bundle &&\  
npm install  
  
USER root  
  
COPY database.yml /var/www/openproject/config/  
COPY configuration.yml /var/www/openproject/config/  
COPY scripts /var/www/openproject/docker/scripts  
  
RUN chown -R openproject:openproject /var/www/openproject &&\  
chmod u+x /var/www/openproject/docker/scripts/*.sh  
  
# Add nginx configuration  
ADD nginx/nginx.conf /etc/nginx/  
ADD nginx/sites-available/openproject.conf /etc/nginx/sites-available/  
RUN chown -R openproject:openproject /etc/nginx/sites-available &&\  
chown -R openproject:openproject /etc/nginx/sites-enabled &&\  
cd /etc/nginx/sites-enabled &&\  
rm default &&\  
ln -s ../sites-available/openproject.conf  
  
# Add supervisord configs  
ADD supervisord/rails.conf /etc/supervisor/conf.d/  
ADD supervisord/nginx.conf /etc/supervisor/conf.d/  
ADD supervisord/delayed_job.conf /etc/supervisor/conf.d/  
  
CMD ["/var/www/openproject/docker/scripts/start_application.sh"]  

