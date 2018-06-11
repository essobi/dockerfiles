FROM robbtraister/watcher  
  
ENV PROCESS="node" \  
ARGUMENTS="."  
  
ONBUILD ADD package.json ./  
ONBUILD RUN npm install --production \  
&& npm cache clean  
  
ONBUILD USER ${USER}  
  
ONBUILD WORKDIR ./src  

