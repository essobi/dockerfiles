FROM asciidoctor/docker-asciidoctor  
MAINTAINER Cedric Gatay <c.gatay@code-troopers.com>  
  
RUN yum install -y gcc-c++ nodejs npm unzip  
RUN gem install --no-ri --no-rdoc haml guard guard-shell guard-livereload
yajl-ruby pygments.rb  
  
RUN curl "https://codeload.github.com/chrisjaure/deckjs-remote/zip/master" -o
master.zip\  
&& unzip master.zip\  
&& rm master.zip\  
&& mv deckjs-remote-master /deck-remote\  
&& cd /deck-remote\  
&& npm install  
  
EXPOSE 9000  
EXPOSE 9010  
EXPOSE 35729  
CMD ln -fs /deck-remote /documents/ && guard start -i & ruby -run -e httpd .
-p 9000& NODE_ENV=production node /deck-remote/server.js 9010  

