FROM ruby:alpine  
  
MAINTAINER Manfred Touron <m@42.am>, based on Simon Weis <docker@w3is.de>  
  
WORKDIR /dashboard  
  
ENV GEM_HOME /dashboard/.bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
  
RUN addgroup smashing \  
&& adduser -S -G smashing smashing \  
&& chown -R smashing:smashing /dashboard  
  
RUN apk update && apk add make gcc g++ nodejs  
  
USER smashing  
  
RUN gem install smashing bundler  
  
ONBUILD COPY . /dashboard  
ONBUILD RUN bundle  
  
EXPOSE 8080  
ENTRYPOINT ["smashing"]  
CMD ["start", "-p", "8080"]  

