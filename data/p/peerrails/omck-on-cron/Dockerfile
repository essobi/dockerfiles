FROM ruby:onbuild  
# Add omck-on-cron  
RUN cd /usr/src/app && bundle install  
  
# Run the command on container startup  
CMD ruby /usr/src/app/job.rb >> /usr/src/app/log.txt  

