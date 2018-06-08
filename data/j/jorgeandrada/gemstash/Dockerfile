FROM ruby:alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="LARP" \  
org.label-schema.description="Gemfile proxy cache" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/gemstash" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run -d --name gemstash -v
/srv/gemstash:/root/.gemstash -p 9292:9292 jorgeandrada/gemstash:latest"  
  
ENV RACK_ENV production  
  
RUN apk add --update build-base \  
sqlite-dev \  
sqlite \  
&& gem install gemstash  
  
EXPOSE 9292  
  
CMD ["gemstash", "start", "--no-daemonize"]  

