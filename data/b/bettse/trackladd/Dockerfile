  
#https://registry.hub.docker.com/_/rails/  
FROM rails:onbuild  
ENV RAILS_ENV production  
  
RUN RAILS_ENV=production bundle exec rake assets:precompile  
RUN echo "America/Los_Angeles" > /etc/timezone && dpkg-reconfigure -f
noninteractive tzdata  
RUN gem install foreman  
  
CMD ["foreman", "start"]  

