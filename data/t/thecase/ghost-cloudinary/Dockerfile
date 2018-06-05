FROM ghost  
  
# install cloudinary module  
RUN npm install cloudinary-store  
RUN mkdir -p /var/lib/ghost/current/core/server/adapters/storage  
RUN cp -r node_modules/cloudinary-store
/var/lib/ghost/current/core/server/adapters/storage  
ENV CLOUDINARY_URL cloudinary://key:secret@account-name  
  
# add configuration  
RUN sed -i 's/^}$/, "storage": { "active": "cloudinary-store", "cloudinary-
store": { "configuration": { "image": { "quality": "auto:good", "secure":
"true" }, "file": { "use_filename": "true", "unique_filename": "false",
"phash": "true", "overwrite": "false", "invalidate": "true" } } } } }/'
/var/lib/ghost/config.production.json  
  
# set site url  
ENV GHOST_URL http://localhost:2368  
COPY docker-entrypoint.sh /usr/local/bin  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 2368  
CMD ["node", "current/index.js"]  

