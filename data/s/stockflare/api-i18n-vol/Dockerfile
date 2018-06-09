FROM ruby:2.3  
MAINTAINER David Kelley <david@stockflare.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV CONFD_VERSION 0.10.0  
ENV INTERVAL 60  
WORKDIR /stockflare  
  
RUN gem install localeapp deep_merge  
  
ADD etc/confd /etc/confd  
  
ADD confd/confd-0.10.0-linux-amd64 /bin/confd  
  
RUN mkdir /stockflare/.localeapp && mkdir /stockflare/locales  
RUN mkdir /stockflare/locales/v1  
RUN mkdir /stockflare/locales/v2  
RUN mkdir /stockflare/locales/v3  
RUN mkdir /stockflare/locales/v4  
RUN mkdir /stockflare/locales/v5  
  
VOLUME /stockflare/locales  
  
ADD boot boot  
  
ADD merge.rb merge.rb  
  
CMD ["./boot"]  

