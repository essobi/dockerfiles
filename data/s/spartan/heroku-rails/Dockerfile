FROM spartan/ruby:latest  
MAINTAINER Colin Rymer <colin.rymer@gmail.com>  
  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
ADD Gemfile* /tmp/  
RUN cd /tmp && bundle install && rm Gemfile*  
RUN gem install foreman  
RUN mkdir /app  
  
WORKDIR /app/  
EXPOSE 5000  
ONBUILD ADD .ruby-version /app/.ruby-version  
ONBUILD ADD Gemfile* /app/  
ONBUILD RUN BUNDLE_JOBS=$(cat /proc/cpuinfo | grep cores | cut -d':' -f2 |
head -n1 | xargs expr -1 +) bundle install  
ONBUILD ADD . /app/  
ONBUILD CMD ["foreman", "start", "web"]  

