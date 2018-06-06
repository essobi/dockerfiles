FROM ruby:alpine  
  
MAINTAINER Simon Weis <docker@w3is.de>  
  
WORKDIR /dashboard  
  
ENV GEM_HOME /dashboard/.bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
  
RUN addgroup dashing \  
&& adduser -S -G dashing dashing \  
&& chown -R dashing:dashing /dashboard  
  
RUN apk update && apk add make gcc g++ nodejs  
  
USER dashing  
  
RUN gem install dashing bundler  
  
ONBUILD COPY . /dashboard  
ONBUILD RUN bundle  
  
EXPOSE 8080  
ENTRYPOINT ["dashing"]  
CMD ["start", "-p", "8080"]  

