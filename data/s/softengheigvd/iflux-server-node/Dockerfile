FROM node:0.12.6-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
# For later use when bower will be reintroduced  
RUN npm install -g grunt bower knex  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /nodejs/iflux && cp -a /tmp/node_modules /nodejs/iflux  
  
ADD . /nodejs/iflux  
  
RUN useradd -m -r -U iflux \  
&& chown -R iflux:iflux /nodejs/iflux \  
&& chmod +x /nodejs/iflux/start.sh  
  
USER iflux  
  
WORKDIR /nodejs/iflux  
  
EXPOSE 3000  
CMD ./start.sh

