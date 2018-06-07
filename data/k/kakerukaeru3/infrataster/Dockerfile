FROM ruby:2.4  
MAINTAINER kakerukaeru "kakerukaeru@gmail.com"  
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

