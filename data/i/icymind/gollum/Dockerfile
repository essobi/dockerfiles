FROM ruby:alpine  
  
RUN set -x && \  
apk --update add \  
build-base cmake icu-dev git tzdata && \  
gem install github-linguist && \  
gem install gollum && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
apk --purge del build-base cmake tzdata && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/wiki"]  
  
EXPOSE 80  
CMD ["gollum"]  

