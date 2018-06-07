FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
# For later use when bower will be reintroduced  
# RUN npm install -g bower  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /nodejs/iflux-slack && cp -a /tmp/node_modules /nodejs/iflux-
slack  
  
ADD . /nodejs/iflux-slack  
  
RUN useradd -m -r -U ifluxslack -u 1111 \  
&& chown -R ifluxslack:ifluxslack /nodejs/iflux-slack  
  
USER ifluxslack  
  
WORKDIR /nodejs/iflux-slack  
  
EXPOSE 3000  
CMD ["npm", "start"]

