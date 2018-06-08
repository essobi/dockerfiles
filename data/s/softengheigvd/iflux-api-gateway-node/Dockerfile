FROM node:0.12.5-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
COPY .npmrc /root/.npmrc  
  
# For later use when bower will be reintroduced  
RUN npm install -g grunt bower  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /nodejs/iflux-api-gateway && cp -a /tmp/node_modules
/nodejs/iflux-api-gateway  
  
ADD . /nodejs/iflux-api-gateway  
  
RUN useradd -m -r -U iflux \  
&& chown -R iflux:iflux /nodejs/iflux-api-gateway  
  
USER iflux  
  
WORKDIR /nodejs/iflux-api-gateway  
  
EXPOSE 3000  
CMD ["npm", "start"]

