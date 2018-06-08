FROM geekle/centos  
ADD . /app  
WORKDIR /app  
RUN bash -lc "bundle install --path vendor/bundle"  
VOLUME ["/var/run/unicorn", "/app"]  
CMD /.rbenv/shims/bundle exec unicorn -p 8080 -c /app/config/unicorn.rb  

