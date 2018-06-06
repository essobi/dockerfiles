FROM debian:jessie  
MAINTAINER Steve Nolen <technolengy@gmail.com>  
# Report issues here: https://github.com/stevenolen/casa-on-rails-docker  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y curl openjdk-7-jre-headless git ruby ruby-dev \  
build-essential libmysqlclient-dev libsqlite3-dev mysql-client sqlite3\  
&& curl --silent --location https://deb.nodesource.com/setup_0.12 | bash - \  
&& apt-get install -y nodejs \  
&& gem install bundler \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV DEPLOY_PATH /var/casa  
RUN git clone https://github.com/ucla/casa-on-rails.git "$DEPLOY_PATH"  
  
WORKDIR $DEPLOY_PATH  
RUN echo '' >> Gemfile && echo "gem 'sqlite3'" >> Gemfile  
RUN bundle install  
RUN npm install  
RUN bundle exec blocks build  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
ADD secrets.yml config/secrets.yml  
ADD ephemeral.rb config/environments/ephemeral.rb  
  
EXPOSE 3000  
CMD ["/run.sh"]

