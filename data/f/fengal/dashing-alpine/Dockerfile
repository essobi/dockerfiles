FROM ruby:2.4.1-alpine  
  
RUN apk add --update g++ make nodejs  
RUN gem install bundler dashing  
RUN mkdir /dashing && \  
dashing new dashing && \  
cd /dashing && \  
bundle  
  
VOLUME ["/dashing"]  
  
ENV PORT 3030  
EXPOSE $PORT  
WORKDIR /dashing  
  
CMD /usr/local/bundle/bin/bundle install; /usr/local/bundle/bin/dashing start  
  

