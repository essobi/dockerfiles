FROM ruby:2.2  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN apt-get update \  
&& apt-get --no-install-recommends -y install \  
libsasl2-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
COPY Gemfile /opt/app/  
WORKDIR /opt/app/  
RUN bundle install \  
&& rspec --init  
  
ENTRYPOINT ["rspec"]  
CMD ["--help"]  

