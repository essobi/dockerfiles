FROM node:4.4.0  
RUN npm install hexo-cli@1.0.2 -g -q && hexo init /blog/ && cd /blog/ && npm
install -q  
  
COPY ./docker-entrypoint.sh /  
WORKDIR /blog  
  
# ezmasterization of hexo  
# see https://github.com/Inist-CNRS/ezmaster  
RUN echo '{ \  
"httpPort": 4000, \  
"configPath": "/blog/_config.json", \  
"dataPath": "/blog/source/_posts/" \  
}' > /etc/ezmaster.json  
  
# # ezmaster need json config  
RUN npm install json2yaml js-yaml -g -q  
RUN js-yaml /blog/_config.yml > /blog/_config.json  
  
EXPOSE 4000  
ENTRYPOINT /docker-entrypoint.sh

