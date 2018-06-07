FROM heroku/cedar:14  
RUN useradd -d /app -m app  
USER app  
WORKDIR /app  
  
ENV HOME /app  
ENV NODE_ENGINE 0.12.6  
ENV PORT 3000  
RUN mkdir -p /app/heroku/node  
RUN mkdir -p /app/src  
RUN curl -s
https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-
linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/heroku/node  
ENV PATH /app/heroku/node/bin:$PATH  
RUN npm i -g npm@2.13.1  
  
RUN mkdir -p /app/.profile.d  
RUN echo "export
PATH=\"/app/heroku/node/bin:/app/bin:/app/src/node_modules/.bin:\$PATH\"" >
/app/.profile.d/nodejs.sh  
RUN echo "cd /app/src" >> /app/.profile.d/nodejs.sh  
WORKDIR /app/src  
  
EXPOSE 3000  
ONBUILD COPY . /app/src  
  
ONBUILD USER root  
ONBUILD RUN chown -R app /app > /dev/null  
ONBUILD USER app  
  
ONBUILD RUN npm prune --production; npm prune --production  

