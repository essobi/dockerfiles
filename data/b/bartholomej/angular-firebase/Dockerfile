FROM node:9-alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL author="Lukas Bartak"  
LABEL maintainer="bart@bartweb.cz"  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MIT" \  
org.label-schema.name="angular-firebase" \  
org.label-schema.description="Lightweight Docker image based on NodeJS 9 with
Angular CLI, Firebase Tools and yarn." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
# Commands  
RUN \  
yarn global add @angular/cli firebase-tools

