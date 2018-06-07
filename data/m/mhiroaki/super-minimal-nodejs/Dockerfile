FROM node:8-onbuild as build  
RUN /usr/src/app/extract /chroot /usr/local/bin/node  
RUN /usr/src/app/extract_node /dep /usr/src/app /chroot  
  
FROM scratch  
COPY \--from=build /chroot /  
COPY \--from=build /dep /  
COPY \--from=build /usr/src/app /usr/src/app  
WORKDIR /usr/src/app  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
CMD [ "node", "index.js" ]  

