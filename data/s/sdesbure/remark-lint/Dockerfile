FROM node:alpine  
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>  
  
ARG VCS_REF=foo  
ARG BUILD_DATE=2018-02-12T16:03:39Z  
  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/remarkjs/remark-lint" \  
org.label-schema.url="https://remark.js.org" \  
org.label-schema.name="ansible lint" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.build-date=$BUILD_DATE  
  
WORKDIR /usr/src/app  
  
RUN apk add --no-cache git && \  
npm install --save remark-cli \  
remark-lint \  
remark-preset-lint-consistent \  
remark-preset-lint-recommended && \  
apk del git  
  
WORKDIR /code  
  
CMD ["/usr/src/app/node_modules/.bin/remark", "--version"]  

