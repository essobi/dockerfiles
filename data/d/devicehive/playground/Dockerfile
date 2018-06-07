FROM phusion/passenger-nodejs:0.9.29  
ARG SOURCE_REPOSITORY_URL  
ARG SOURCE_BRANCH  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Expose Nginx HTTP service  
EXPOSE 8080  
# Enable nginx and remove the default site  
RUN rm -f /etc/service/nginx/down \  
&& rm /etc/nginx/sites-enabled/default  
  
# copy playground website files  
RUN mkdir /home/app/playground \  
&& cd /home/app/playground \  
&& curl -L "${SOURCE_REPOSITORY_URL:-https://github.com/devicehive/devicehive-
playground}/archive/${SOURCE_BRANCH:-master}.tar.gz" | tar -zxf - --strip-
components=1 \  
&& npm install . \  
&& npm cache clean --force \  
&& chown -R app:app /home/app/playground  
  
# Install freeboard and DeviceHive datastore  
RUN mkdir -p /home/app/freeboard/dashboard \  
&& cd /home/app/freeboard/dashboard \  
&& curl -L https://github.com/devicehive/freeboard/archive/master.tar.gz | tar
-zxf - --strip-components=1 \  
&& npm install . \  
&& npm install -g grunt-cli \  
&& grunt \  
&& npm cache clean --force \  
&& mkdir -p /home/app/freeboard/dashboard/plugins/devicehive-freeboard-
datasource \  
&& cd /home/app/freeboard/dashboard/plugins/devicehive-freeboard-datasource \  
&& curl -L https://github.com/devicehive/devicehive-freeboard-
datasource/archive/master.tar.gz | tar -zxf - --strip-components=1 \  
&& chown -R app:app /home/app/freeboard/dashboard  
  
# register playground website in nginx  
ADD playground.conf /etc/nginx/sites-enabled/playground.conf  
ADD perl-variables.conf /etc/nginx/conf.d/perl-variables.conf  
ADD nginx-env.conf /etc/nginx/main.d/nginx-env.conf  

