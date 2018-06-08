FROM ruby:alpine  
LABEL mainteiner Yuto Urakami <urakami@loilo.tv>  
  
ENV ROOT_PATH /usr/src/web-shrinker-scraper  
ENV APP_PATH ${ROOT_PATH}/app  
  
COPY app/* ${APP_PATH}/  
COPY run.sh /  
COPY docker-entrypoint.sh /  
  
RUN apk add --no-cache build-base libxml2-dev libxslt-dev \  
&& chmod +x /docker-entrypoint.sh \  
&& chmod +x /run.sh \  
&& gem install nokogiri \  
&& gem install mechanize  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

