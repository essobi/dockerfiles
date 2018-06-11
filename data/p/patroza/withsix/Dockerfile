FROM patroza/node-npm:8.1.4 as builder  
  
WORKDIR /opt/frontend/app  
  
# TODO: Make this a separate image too? incl creating the legacy and libs...  
# So probably a legacy directory next to app and server?  
RUN npm install -g bower  
COPY ./frontend/app/bower.json /opt/frontend/app/  
RUN bower --allow-root install --config.interactive=false  
  
COPY ./frontend/app/package.json ./frontend/app/package-lock.json
/opt/frontend/app/  
COPY ./withsix-sync-api-js/package.json ./withsix-sync-api-js/package-
lock.json /opt/withsix-sync-api-js/  
COPY ./mediatr-js/package.json ./mediatr-js/package-lock.json /opt/mediatr-js/  
  
RUN npm run full-install  
  
COPY ./frontend/app/legacy/ /opt/frontend/app/legacy/  
COPY ./frontend/app/Gruntfile.js /opt/frontend/app/  
RUN npm run build-bower  
COPY ./frontend/app/src_legacy/vendor/ /opt/frontend/app/src_legacy/vendor/  
RUN npm run build-legacy  
  
COPY ./frontend/app/src_legacy/app/ /opt/frontend/app/src_legacy/app/  
RUN npm run build-app  
  
# We have to move it here, because we will overlay the local copy of that
folder again at the next COPY command  
RUN mkdir -p /opt/server/public && mv legacy /opt/server/public/  
  
COPY ./frontend/app/ /opt/frontend/app/  
COPY ./withsix-sync-api-js/ /opt/withsix-sync-api-js/  
COPY ./mediatr-js/ /opt/mediatr-js/  
  
RUN npm run dist  
  
RUN mv dist/index.html /opt/server/index.html && mv dist/*.*
/opt/server/public/ && mv img/ /opt/server/public/  
  
FROM patroza/node-npm-alpine:8.1.4  
COPY \--from=builder /opt/server /opt/server/  
  
WORKDIR /opt/server  
COPY ./frontend/server/package.json ./frontend/server/package-lock.json
/opt/server/  
COPY ./frontend/server/build/ /opt/server/build/  
RUN npm install  
  
COPY ./frontend/server/ /opt/server/  
  
# TODO: We should change the versioning to the git short hash?  
RUN node build/bump.js  
  
# TODO: Doing stuff on Azure seems to require a bit more plumbing..  
# https://github.com/Azure-App-
Service/node/blob/master/8.1.2/startup/init_container.sh  
EXPOSE 80  
CMD ["npm", "start"]  

