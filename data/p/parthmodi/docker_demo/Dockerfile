FROM parthmodi/rails_base:latest  
  
RUN apt-get update && \  
apt-get install -y libpq-dev imagemagick && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
ENV RAILS_LOG_TO_STDOUT true  
  
# Workdir  
RUN mkdir -p /home/app  
WORKDIR /home/app  
  
# Install gems  
ADD Gemfile* /home/app/  
ADD docker /home/app/docker/  
RUN bundle install  
  
# Add the Rails app  
ADD . /home/app  
  
# Precompile assets  
RUN RAILS_ENV=production bundle exec rake assets:precompile --trace  
  
# # Create user and group  
RUN groupadd --gid 9999 app && \  
useradd --uid 9999 --gid app app && \  
chown -R app:app /home/app  
  
# Save timestamp of image building  
RUN date -u > BUILD_TIME  
  
ENV RAILS_LOG_TO_STDOUT true  
ENV RAILS_SERVE_STATIC_FILES false  
  
# RUN mkdir -p /etc/nginx/conf.d/  
# COPY docker/nginx.conf /etc/nginx/conf.d/default.conf  
RUN chmod +x docker/entrypoint.sh  
ENV APPNAME docker_demo  
  
EXPOSE 3000  
CMD [ "docker/entrypoint.sh" ]

