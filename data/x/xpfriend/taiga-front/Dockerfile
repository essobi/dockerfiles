FROM nginx:1.13.3-alpine  
MAINTAINER ototadana@gmail.com  
  
ENV GIT_VERSION 2.11.3-r0  
ENV TAIGA_BRANCH stable  
ENV TAIGA_FRONT_VERSION b3f15414fa826aee7ca0ef179b25c209a5a40224  
  
RUN apk add --no-cache git=${GIT_VERSION}  
  
RUN mkdir /taiga \  
&& git clone https://github.com/xpfriend/taiga-front-dist.git /taiga/taiga-
front-dist \  
&& cd /taiga/taiga-front-dist \  
&& git checkout ${TAIGA_BRANCH} \  
&& echo "${TAIGA_FRONT_VERSION}" > /taiga/version  
  
COPY ./bin/. /taiga/bin/  
RUN chmod +x /taiga/bin/*  
  
CMD ["/bin/sh", "/taiga/bin/start.sh"]  

