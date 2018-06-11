FROM vantienvnn/laravel5-docker-build:latest  
  
# Apply Nginx configuration  
RUN apt-get update \  
&& apt-get install -y postgresql postgresql-contrib \  
&& apt-get remove -y nodejs \  
&& touch /init-start.sh && rm -f /init-start.sh \  
&& chsh -s /bin/bash jenkins  
  
# run install nodejs 7  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs build-essential  
  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/
\  
&& rm -r /etc/ssl/private \  
&& mv /etc/ssl/private-copy /etc/ssl/private \  
&& chmod -R 0700 /etc/ssl/private \  
&& chown -R postgres /etc/ssl/private  
  
# install yarn  
RUN npm install -g yarn  
  
ADD config/init-start.sh /init-start.sh  
RUN chmod +x /init-start.sh  
# Default command  
ENTRYPOINT ["/init-start.sh"]  
  

