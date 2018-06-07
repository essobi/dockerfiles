FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
RUN npm install -g grunt-cli  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /apidoc && cp -a /tmp/node_modules /apidoc  
  
COPY . /apidoc  
  
RUN cd /apidoc \  
&& grunt prod --baseUrl="{{ site.baseurl }}/api"  
  
RUN useradd -m -r -U iflux \  
&& chown -R iflux:iflux /apidoc  
  
USER iflux  
  
WORKDIR /apidoc  
  
EXPOSE 4000  
CMD [ "grunt", "serve", "--host=0.0.0.0" ]  

