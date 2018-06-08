FROM ruby:2.3-alpine  
  
ARG GIT_VERSION  
ARG BUILD_DATE  
  
LABEL io.github.oshuma.scumbag.web.git-version=$GIT_VERSION \  
io.github.oshuma.scumbag.web.build-date=$BUILD_DATE  
  
LABEL org.label-schema.vcs-ref=$GIT_VERSION \  
org.label-schema.vcs-url="https://github.com/Oshuma/scumbag-docker"  
  
RUN apk add --update --no-cache \  
build-base \  
postgresql-dev \  
nodejs \  
tzdata \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /app/web  
WORKDIR /app/web  
  
COPY scumbag /app/web  
  
RUN bundle install  

