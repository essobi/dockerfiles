FROM alpine:latest  
MAINTAINER Vipin Madhavanunni <vipintm@gmail.com>  
LABEL site="unwsolution.com" \  
version="1.0" \  
description="Jekyll Docker image" \  
source="https://github.com/UNwS/jekyll-docker"  
  
# default source  
ENV page="https://github.com/thekkedam/vm"  
# Install all the dependencies for Jekyll  
RUN apk add --update bash build-base libffi libffi-dev zlib zlib-dev libxml2
libxml2-dev \  
libxslt libxslt-dev ruby ruby-dev ruby-io-console ruby-json \  
yaml nodejs git perl  
  
# let avoide rdoc  
RUN echo 'gem: --no-document' >> ~/.gemrc && \  
cp ~/.gemrc /etc/gemrc && \  
chmod uog+r /etc/gemrc  
  
# Install bundler  
RUN gem install bundler  
  
# Install nokogiri seperate  
# RUN gem install nokogiri -- --use-system-libraries --with-
xml2-include=/usr/include/libxml2 --with-xml2-lib=/usr/lib/  
# Get gemfile to get all suported pakage for jekyll in gethub pages  
WORKDIR /tmp  
COPY Gemfile Gemfile  
COPY build build  
  
# lets install all required gems  
# RUN bundle config build.nokogiri --use-system-libraries  
RUN bundle config build.jekyll --no-rdoc  
RUN bundle install  
  
# lets clean  
RUN find / -type f -iname \\*.apk-new -delete && \  
rm -rf /var/cache/apk/* && \  
rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \  
rm -rf ~/.gem  
  
# Copy source  
RUN mkdir -p /html  
VOLUME ["/html"]  
WORKDIR /html  
  
# Run jekyll serve  
ENTRYPOINT ["/tmp/build", "-d", "$page"]  
  

