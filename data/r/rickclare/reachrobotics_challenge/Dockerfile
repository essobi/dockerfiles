FROM ruby:2.3.1-alpine  
ENTRYPOINT ["/bin/ash", "-c"]  
  
RUN apk --no-cache add \  
build-base \  
git \  
libxml2-dev \  
libxslt-dev \  
readline-dev \  
ruby-tzinfo \  
sqlite-dev  
  
## set timezone: https://wiki.alpinelinux.org/wiki/Setting_the_timezone  
RUN cp /usr/share/zoneinfo/Europe/London /etc/localtime \  
&& echo "Europe/London" > /etc/timezone  
  
RUN gem update --system && \  
gem install bundler foreman  
  
ENV PATH=./bin:$PATH \  
RAILS_ENV=docker \  
RACK_ENV=docker  
  
WORKDIR /myapp  
COPY Gemfile Gemfile.lock /myapp/  
RUN bundle config build.nokogiri --use-system-libraries && \  
bundle config without production:staging:demo && \  
bundle config jobs 3 && \  
bundle install  
  
COPY . /myapp  
  
RUN rails db:reset  
  
## cleanup  
RUN rm -rf /tmp/* /var/tmp/*  

