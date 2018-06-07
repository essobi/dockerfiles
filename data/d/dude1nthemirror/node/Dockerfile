FROM node:6.9.1  
MAINTAINER dudeinthemirror  
  
COPY ./.vimrc /root/.vimrc  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv D101F7899D41F3C3  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install yarn=0.16.1-1 && apt-get clean  
  
RUN cd /usr/local/lib/node_modules && \  
mv npm /tmp && \  
curl -L registry.npmjs.com/npm/-/npm-{3.10.7}.tgz | tar xz
--transform="s:^package:npm:"  
RUN echo "Y" | apt-get install vim-tiny  

