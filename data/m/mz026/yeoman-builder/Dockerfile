# docker run -it --rm -v $(pwd):/app -v $(pwd)/node_modules:/app/node_modules
-w /app yeoman-builder:latest npm install  
# docker run -it --rm -v $(pwd):/app -v
$(pwd)/bower_components:/app/bower_components -w /app yeoman-builder:latest
bower --allow-root --config.interactive=false install  
FROM ruby:2.1  
RUN gem install compass  
  
ENV NODE_VERSION 0.10.33  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
  

