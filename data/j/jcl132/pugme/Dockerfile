FROM ruby:2.2.6  
MAINTAINER Subbu <subbarao.kly@gmail.com>  
ENV REFRESHED_AT 2016-10-24  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# for postgres  
RUN apt-get install -y libpq-dev  
  
# for nokogiri  
RUN apt-get install -y libxml2-dev libxslt1-dev  
  
# for capybara-webkit  
RUN apt-get install -y libqt4-webkit libqt4-dev xvfb  
  
# for node  
RUN apt-get install -y python python-dev python-pip python-virtualenv  
  
RUN wget -qO- https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
RUN apt-get install apt-transport-https  
  
# Download and Install Nginx  
#RUN apt-get install -y nginx  
# Remove the default Nginx configuration file  
#RUN rm -v /etc/nginx/nginx.conf  
# Copy a configuration file from the current directory  
#ADD nginx.conf /etc/nginx/  
# Append "daemon off;" to the beginning of the configuration  
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
# cleanup  
RUN rm -rf /var/lib/apt/lists/*  
  
# install nodejs  
#RUN \  
# cd /tmp && \  
# wget http://nodejs.org/dist/node-latest.tar.gz && \  
# tar xvzf node-latest.tar.gz && \  
# rm -f node-latest.tar.gz && \  
# cd node-v* && \  
# ./configure && \  
# CXX="g++ -Wno-unused-local-typedefs" make && \  
# CXX="g++ -Wno-unused-local-typedefs" make install && \  
# cd /tmp && \  
# rm -rf /tmp/node-v* && \  
# npm install -g npm && \  
# echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install yarn  
  
#RUN mkdir -p /var/run/postgresql  
#&& chown -R postgres:postgres /var/run/postgresql && chmod g+s
/var/run/postgresql  
WORKDIR /app  
  
COPY . /app  
  
# Prevent bundler warnings; ensure that the bundler version executed is >=
that which created Gemfile.lock  
RUN gem install bundler  
  
# Finish establishing our Ruby enviornment  
RUN bundle install  
  
RUN yarn install  
  
# Temporary. Will be moved to base image later.  
ENV RACK_ENV=production \  
RAILS_ENV=production  
  
# Run asset pipeline if we're in a Rails app.  
#RUN if test -d app/assets -a -f config/application.rb; then \  
# bundle exec rake assets:precompile || true; \  
#fi  
#RUN bundle exec rake assets:precompile  
# Expose ports  
EXPOSE 5432  
#EXPOSE 8080  
ENV PORT=8080  
#ENV POSTGRES_PASSWORD="rLNNEDqPDm57344J"  
#ENV POSTGRES_USER="postgres"  
ENTRYPOINT []  
CMD []  
  
CMD ["foreman", "start", "-f", "Procfile"]  
#CMD ["rails", "server", "Puma", "-p", "8080"]

