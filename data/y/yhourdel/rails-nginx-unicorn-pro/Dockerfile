# Dockerfile  
FROM seapy/rails-nginx-unicorn-pro:v1.1-ruby2.3.0-nginx1.8.1  
# override cmd  
CMD bundle exec rake assets:precompile && rm -f /app/tmp/unicorn.pid &&
foreman start -f Procfile  

