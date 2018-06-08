FROM ruby:2.4-alpine  
LABEL maintainer="cdower"  
EXPOSE 3000  
COPY ./ /app/  
  
WORKDIR /app  
RUN apk update \  
&& apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv \  
&& apk add --no-cache zlib gcc g++ musl-dev libxml2-dev libxslt-dev make
sqlite sqlite-dev nodejs tzdata \  
&& echo "Etc/UTC" > /etc/timzone  
  
RUN gem install bundler execjs therubyracer \  
&& bundle config build.nokogiri --use-system-libraries \  
&& bundle install --system  
  
CMD rake db:migrate && bin/rails server  

