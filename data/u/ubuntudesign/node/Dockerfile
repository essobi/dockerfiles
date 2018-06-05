FROM node:6-slim  
  
WORKDIR /app  
ENTRYPOINT ["/entrypoint"]  
  
ENV APP_MODULES="/packages/node_modules"  
ENV HASH_FILE="$APP_MODULES/package.json.hash"  
ENV OVERRIDES="/packages/overrides"  
ENV NODE_PATH="${OVERRIDES}:${APP_MODULES}"  
ENV SASS_PATH="${NODE_PATH}"  
ENV PATH="${OVERRIDES}/.bin:${APP_MODULES}/.bin:/bin:${PATH}"  
RUN mkdir -p $APP_MODULES  
RUN mkdir -p $OVERRIDES/.bin  
RUN ln -s /app/package.json /packages/package.json  
  
ADD USAGE.md /USAGE.md  
ADD bin /bin/  
ADD entrypoint /entrypoint  

