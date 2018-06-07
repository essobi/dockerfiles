FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
# For later use when bower will be reintroduced  
RUN npm install -g bower  
  
ADD . /nodejs/ifluxfe  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/ (similar approach for bower)  
ADD bower.json /tmp/bower.json  
RUN cd /tmp && bower install --allow-root  
RUN mkdir -p /nodejs/ifluxfe/public/components && cp -a
/tmp/bower_components/* /nodejs/ifluxfe/public/components  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN cp -a /tmp/node_modules /nodejs/ifluxfe  
  
RUN useradd -m -r -U ifluxfe -u 1116 \  
&& chown -R ifluxfe:ifluxfe /nodejs/ifluxfe  
  
USER ifluxfe  
  
WORKDIR /nodejs/ifluxfe  
  
EXPOSE 3000  
CMD ["npm", "start"]

