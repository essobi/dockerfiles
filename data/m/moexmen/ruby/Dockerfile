FROM ruby:2.4-alpine3.7  
  
ENV TZ Asia/Singapore  
  
RUN \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \  
&& apk --update add postgresql-client \  
nodejs \  
tzdata \  
libxml2 \  
libxslt \  
curl \  
&& apk --update add --virtual build-dependencies \  
git \  
openssh-client \  
build-base \  
postgresql-dev \  
libxml2-dev \  
libxslt-dev \  
&& bundle config --global jobs 4 \  
&& adduser -S -h /app -u 10000 app  
  
WORKDIR /app/  
  
CMD [ "irb" ]  

