FROM alpine:3.6  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://bitbucket.org/yusufhm/reins" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="0.1.0"  
  
EXPOSE 3000  
# add user & install system dependencies.  
RUN addgroup -g 1000 node && \  
adduser -u 1000 -G node -D node && \  
apk add --no-cache \  
py2-pip curl nodejs-npm openssh-client python && \  
apk add --no-cache --virtual .build-deps \  
gcc libffi-dev musl-dev openssl-dev perl python-dev make && \  
pip install ansible && \  
apk del .build-deps  
  
# add & install nodejs dependencies.  
COPY www/package.json /tmp/package.json  
RUN cd /tmp && npm install && npm cache clean && \  
mkdir -p /app/www && \  
cp -a /tmp/node_modules /app/www  
  
# add the rest of the app files  
COPY ansible /app/ansible  
COPY www /app/www  
  
WORKDIR /app/www  
  
USER node  
  
CMD [ "npm", "start" ]  

