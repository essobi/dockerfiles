FROM phusion/passenger-ruby23  
  
MAINTAINER Dmitry Ustalov <dmitry.ustalov@gmail.com>  
  
EXPOSE 80  
CMD ["/sbin/my_init"]  
  
ENV RACK_ENV=production LANG=en_US.utf8  
  
WORKDIR /home/app/petrovich  
  
COPY . /home/app/petrovich/  
  
RUN \  
bundle install --deployment --without 'development test' \--jobs 4 && \  
mv -fv docker/petrovich.conf /etc/nginx/sites-enabled/petrovich.conf && \  
rm -f /etc/nginx/sites-enabled/default /etc/service/nginx/down && \  
mkdir -p /home/app/petrovich/log && \  
bin/rake assets:precompile && \  
rm -rf /tmp/* /var/tmp/* && \  
chown -R app:app /home/app  

