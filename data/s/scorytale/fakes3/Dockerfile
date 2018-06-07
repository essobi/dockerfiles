FROM alpine:3.6  
MAINTAINER ScoryTale <developers@sportintown.com>  
  
RUN apk add --no-cache --update \  
ruby ruby-dev ruby-bundler \  
python py-pip \  
git build-base libxml2-dev libxslt-dev  
  
RUN pip install boto s3cmd  
  
ENV GEM_HOME=/gems  
  
RUN gem install --no-document fakes3  
RUN ln -s /gems/bin/fakes3 /usr/local/bin/fakes3  
  
RUN mkdir -p /storage  
  
EXPOSE 4569  
CMD ["fakes3", "-r", "/storage", "-p", "4569"]  
  

