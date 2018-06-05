FROM heroku/cedar:14  
MAINTAINER Atsushi Nagase<ngs@mov.am>  
  
ENV NODE_ENGINE 0.10.48  
ENV PATH /app/heroku/node/bin/:/app/user/node_modules/.bin:$PATH  
  
RUN mkdir -p /app/heroku/node /app/.profile.d  
WORKDIR /app/user  
  
RUN curl -s
https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-
linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/heroku/node  
RUN echo "export
PATH=\"/app/heroku/node/bin:/app/user/node_modules/.bin:\$PATH\"" >
/app/.profile.d/nodejs.sh  
  
RUN wget https://cli-assets.heroku.com/branches/stable/heroku-linux-
amd64.tar.gz -O heroku.tar.gz && \  
mkdir -p /usr/local/lib && \  
tar -xvzf heroku.tar.gz -C /usr/local/lib && \  
rm -f heroku.tar.gz && \  
/usr/local/lib/heroku/install  

