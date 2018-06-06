FROM itzco/docker_node  
  
MAINTAINER itzco <mritzco@gmail.com>  
  
WORKDIR /src  
  
RUN /bin/bash -c ' source /root/.nvm/nvm.sh \  
&& [ -f package.json ] && npm install --production || echo "package.json not
found " \  
&& [ -f bower.json ] && bower install --production || echo "bower.json not
found" \  
'  
  
VOLUME ["/src"]  
  
ENTRYPOINT ["/usr/entry.sh"]  
CMD ["index.js"]  

