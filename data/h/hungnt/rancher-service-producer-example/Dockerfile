FROM iojs:onbuild  
MAINTAINER hungnt-me@gmail.com  
  
RUN npm install  
  
ENV RETHINKDB_HOST=rethinkdb  
ENV RETHINKDB_PORT=28015  
ENV RETHINKDB_DB=rancher_demo  
ENV PORT=80  
CMD ["node", "app.js"]  
  
# Expose the ports that your app uses. For example:  
EXPOSE 80  

