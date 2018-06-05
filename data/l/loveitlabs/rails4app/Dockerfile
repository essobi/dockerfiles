FROM loveitlabs/rails-server:latest  
MAINTAINER LoveItLabs Team <team@loveitlabs.io>  
  
WORKDIR /$APPROOT  
ENV APPROOT app  
  
#By putting this at the beginning of the file, you can add ENV directives  
#or other commands and not invalidate the bundle cache- saving you a lot of
pain.  
ADD Gemfile /$APPROOT/  
ADD Gemfile.lock /$APPROOT/  
ENV BUNDLE_PATH=/bundle  
RUN bundle config --global --jobs 16 &&\  
bundle install -j16  
  
ENV TERM vt100  
#ENV RAILS_ENV staging  
ENV RAILS_ENV production  
  
# Output of `rake secret` Should really be passed in as params and only stored
in super secret encrypted vault.  
# Set these up in config/secrets.yml Some apps don't have a stage environment
by default- but they probably should ;)  
ENV SECRET_KEY_BASE_STAGE
8698fca2fbf1e8d713cef827e9445915f03f7cdabc663fd24ac68a9c2a349fa910baa441115d76b138f24e504f9982c21adf1a8911578b57adfc656bb42e1716  
ENV SECRET_KEY_BASE_PROD
f491fdf0e84319cb40d980627912d3bbe5a32c44ee98625182a5a057bafa53c9dce3ea4d5e9f5e3455429f4cdd16a9e4003c35f88dcaa3755e7cd4f8ceb46e82  
  
  
#Add the rails application to the docker image.  
ADD nginx.vhost /etc/nginx/sites-enabled/  
ADD config /$APPROOT/  
ADD Rakefile /$APPROOT/  
ADD . /$APPROOT/  
  
#supervisor already installed in base image.  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD cd /app &&\  
bundle exec rake assets:precompile &&\  
#bundle exec rake user:add_roles &&\  
#bundle exec rake script:add_context &&\  
bundle exec rake db:migrate &&\  
bash -c "/usr/bin/supervisord -c /app/supervisord.conf"  
  
EXPOSE 80  

