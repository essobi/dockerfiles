FROM ruby:alpine  
  
MAINTAINER The U-TEST Team  
# base on Dockerfile shifudao/gollum with 'textile' support  
RUN apk update && \  
apk add make gcc g++ icu-libs icu-dev git && \  
gem install gollum org-ruby RedCloth && \  
apk del make gcc g++ icu-dev && \  
rm -fr /var/cache/apk/* /usr/local/bundle/cache /root/.gem/ /root/.gemrc
/root/.ash_history && \  
find /usr/local/bundle/ \\( -name 'gem_make.out' -o -name 'mkmf.log' \\)
-delete && \  
mkdir /wiki  
  
COPY config.rb /usr/local/etc/  
COPY req.rb /usr/local/etc/  
  
EXPOSE 4567  
# use ENTRYPOINT instead CMD allows to pass arguments to entry point  
ENTRYPOINT ["gollum", "--config", "/usr/local/etc/config.rb" ]  
CMD []  

