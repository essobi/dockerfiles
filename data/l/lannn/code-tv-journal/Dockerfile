FROM emachnic/code_tv  
  
WORKDIR /tmp  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN /bin/bash -l -c "bundle install"  
  
ADD ./ /var/www/journal  
ADD config/journal.conf /etc/nginx/sites-enabled/journal  
ADD config/start_server.sh /usr/bin/start_server  
RUN chmod +x /usr/bin/start_server  
RUN mkdir -p /var/www/journal/tmp/pids  
RUN mkdir -p /var/www/journal/tmp/sockets  
RUN mkdir -p /var/www/journal/log  
  
WORKDIR /var/www/journal  
  
EXPOSE 80  
ENTRYPOINT /usr/bin/start_server  
  

