FROM circleci/php:7.1-cli-node-browsers  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://bitbucket.org/yusufhm/reins" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="0.1.0"  
  
RUN composer global require hirak/prestissimo && \  
sudo npm install -g grunt-cli gulp-cli  

