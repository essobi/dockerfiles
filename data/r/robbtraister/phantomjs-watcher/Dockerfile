FROM robbtraister/watcher  
  
ADD phantomjs.tar.bz2 /  
RUN phantomjs -v  
  
ENV PROCESS="phantomjs" \  
ARGUMENTS="index.js"  
  
USER ${USER}  
  
WORKDIR ./src  

