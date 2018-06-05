FROM heroku/cedar:14  
RUN useradd -d /app -m app  
USER app  
WORKDIR /app  
  
ENV HOME /app  
ENV NODE_ENGINE 0.10.29  
ENV PORT 9000  
RUN mkdir -p /app/heroku/node  
RUN mkdir -p /app/src  
RUN curl -s
https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-
linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/heroku/node  
ENV PATH /app/heroku/node/bin:$PATH  
  
RUN mkdir -p /app/.profile.d  
RUN echo "export
PATH=\"/app/heroku/node/bin:/app/bin:/app/src/node_modules/.bin:\$PATH\"" >
/app/.profile.d/nodejs.sh  
RUN echo "cd /app/src" >> /app/.profile.d/nodejs.sh  
WORKDIR /app/src  
  
# We use exec here so that Ctrl-C works to exit the process.  
CMD exec node server.js  
EXPOSE 9000  
COPY camo /app/src  
RUN npm install  

