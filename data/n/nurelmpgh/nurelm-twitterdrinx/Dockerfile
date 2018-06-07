FROM shaabans/nurelm-dockerbase-nginx-ruby-node  
  
# Doing this lets bundle cache  
WORKDIR /tmp  
ADD ruby/Gemfile Gemfile  
ADD ruby/Gemfile.lock Gemfile.lock  
RUN /bin/bash -l -c "bundle install"  
  
# Setup Ngnix and Unicorn  
ADD ./ /var/www/twitterthang  
ADD config/twitterthang.conf /etc/nginx/sites-enabled/twitterthang  
ADD config/start_server.sh /usr/bin/start_server  
RUN chmod +x /usr/bin/start_server  
RUN mkdir -p /var/www/twitterthang/ruby/tmp/pids  
RUN mkdir -p /var/www/twitterthang/ruby/tmp/sockets  
RUN mkdir -p /var/www/twitterthang/ruby/log  
  
# Run first search and setup search cron job  
RUN ruby /var/www/twitterthang/ruby/search_tweets.rb  
ADD config/search-cron /etc/cron.d/twitterthang  
RUN cron  
  
WORKDIR /var/www/twitterthang  
EXPOSE 80  
CMD /usr/bin/start_server  

