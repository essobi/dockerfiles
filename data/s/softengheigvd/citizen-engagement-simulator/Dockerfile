FROM node:0.12.0-wheezy  
MAINTAINER Laurent Prevost <laurent.prevost@heig-vd.ch>  
  
RUN npm install -g api-copilot-cli  
  
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-
dot-js/  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /nodejs/citizen-simulator && cp -a /tmp/node_modules
/nodejs/citizen-simulator  
  
ADD . /nodejs/citizen-simulator  
  
RUN useradd -m -r -U citizen \  
&& chown -R citizen:citizen /nodejs/citizen-simulator \  
&& chmod +x /nodejs/citizen-simulator/run.sh  
  
USER citizen  
  
WORKDIR /nodejs/citizen-simulator  
  
CMD ["./run.sh"]

