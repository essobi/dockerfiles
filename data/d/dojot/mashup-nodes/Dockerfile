FROM nodered/node-red-docker  
  
RUN cd /usr/src/node-red/node_modules/node-red/nodes/core; \  
find -name '*.html' | \  
grep -v -e 'template' | \  
awk '{system("mv "$1" "$1".ign")}';  
RUN cd /usr/src/node-red/node_modules; ls -1 | grep 'node-red-node' | xargs rm
-rf  
COPY node_modules /data/node_modules  

