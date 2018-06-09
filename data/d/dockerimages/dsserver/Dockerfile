FROM node:latest  
ADD . /server  
RUN /bin/sh -c "(cd $(npm root -g)/npm && npm install fs-extra && sed -i -e
s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/ ./lib/utils/rename.js)"  
WORKDIR /server  
RUN npm install  
ENTRYPOINT ["/server/bin/dssrv"]  
CMD ["-h"]  

