FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
# For later use when bower will be reintroduced  
RUN npm install -g bower  
  
ADD . /nodejs/viewbox  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/ (similar approach for bower)  
ADD bower.json /tmp/bower.json  
RUN cd /tmp && bower install --allow-root  
RUN mkdir -p /nodejs/viewbox/public/components && cp -a
/tmp/bower_components/* /nodejs/viewbox/public/components  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN cp -a /tmp/node_modules /nodejs/viewbox  
  
RUN useradd -m -r -U viewbox -u 1113 \  
&& chown -R viewbox:viewbox /nodejs/viewbox  
  
USER viewbox  
  
WORKDIR /nodejs/viewbox  
  
EXPOSE 3000  
CMD ["npm", "start"]

