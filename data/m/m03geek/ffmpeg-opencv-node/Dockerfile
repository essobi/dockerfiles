ARG VERSION  
FROM mhart/alpine-node:${VERSION} as nodebase  
  
FROM m03geek/ffmpeg-opencv:alpine  
ENV OPENCV4NODEJS_DISABLE_AUTOBUILD=1  
  
COPY --from=nodebase /usr/bin/node /usr/bin/  
COPY --from=nodebase /usr/lib/node_modules /usr/lib/node_modules  
COPY --from=nodebase /usr/include/* /usr/include/  
  
RUN ln -s /usr/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm \  
&& ln -s /usr/lib/node_modules/npm/bin/npx-cli.js /usr/bin/npx \  
&& rm -rf /usr/local/lib && ln -s /usr/local/lib64 /usr/local/lib \  
&& rm /usr/lib/node_modules/npm/*.md  

