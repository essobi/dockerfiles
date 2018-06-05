FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
# For later use when bower will be reintroduced  
# RUN npm install -g bower  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /nodejs/iflux-metrics && cp -a /tmp/node_modules /nodejs/iflux-
metrics  
  
ADD . /nodejs/iflux-metrics  
  
RUN useradd -m -r -U metrics -u 1114 \  
&& chown -R metrics:metrics /nodejs/iflux-metrics  
  
USER metrics  
  
WORKDIR /nodejs/iflux-metrics  
  
EXPOSE 3000  
CMD ["npm", "start"]

