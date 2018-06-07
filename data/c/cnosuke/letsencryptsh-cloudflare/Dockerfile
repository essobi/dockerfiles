FROM ruby:2.3-alpine  
MAINTAINER cnosuke  
  
RUN apk update  
RUN apk add --no-cache bash openssl git libcurl gcc make g++ zlib-dev curl-dev
curl  
RUN git clone \--depth 1 https://github.com/lukas2511/dehydrated.git  
RUN mkdir -p dehydrated/certs && ln -s /dehydrated/certs /certs  
ADD cloudflare-hook ./cloudflare-hook  
RUN cd cloudflare-hook && bundle install  
ADD run.sh .  
  
VOLUME ['/certs']  
  
CMD ["./run.sh"]  
  
# docker run --rm --env-file envs -v path_to_certs_on_host:/certs
cnosuke/letsencryptsh-cloudflare  

