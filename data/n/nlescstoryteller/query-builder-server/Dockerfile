FROM nlescstoryteller/storyteller  
  
VOLUME /data  
  
COPY . /src/query-builder-server/  
  
WORKDIR /src/query-builder-server/  
RUN yarn install  
RUN yarn add sqlite3  
  
WORKDIR /src/query-builder-server/sqlite/funcs/  
RUN tar -xvzf /src/query-builder-server/node_modules/sqlite3/deps/sqlite-
autoconf-3150000.tar.gz sqlite-autoconf-3150000/sqlite3.h  
RUN tar -xvzf /src/query-builder-server/node_modules/sqlite3/deps/sqlite-
autoconf-3150000.tar.gz sqlite-autoconf-3150000/sqlite3ext.h  
RUN mv sqlite-autoconf-3150000/sqlite3.h sqlite-autoconf-3150000/sqlite3ext.h
.  
RUN rm -rf sqlite-autoconf-3150000  
RUN gcc -lm -fPIC -shared xenon_functions.c -o libxenonfunctions.so
-L./sqlite3.h -L./sqlite3ext.h  
  
WORKDIR /src/query-builder-server  
EXPOSE 5000  
CMD ["npm", "start"]  

