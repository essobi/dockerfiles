FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
# For later use when bower will be reintroduced  
# RUN npm install -g bower  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /nodejs/citizen-engagement && cp -a /tmp/node_modules
/nodejs/citizen-engagement  
  
ADD . /nodejs/citizen-engagement  
  
RUN useradd -m -r -U citizen -u 1112 \  
&& chown -R citizen:citizen /nodejs/citizen-engagement  
  
USER citizen  
  
WORKDIR /nodejs/citizen-engagement  
  
EXPOSE 3000  
CMD ["npm", "start"]

