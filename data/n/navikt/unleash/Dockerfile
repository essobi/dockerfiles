# gjør det mulig å bytte base-image slik at vi får bygd både innenfor og
utenfor NAV  
ARG BASE_IMAGE_PREFIX=""  
FROM ${BASE_IMAGE_PREFIX}node  
  
ADD . /  
  
ENV NODE_TLS_REJECT_UNAUTHORIZED=0  
RUN npm install --unsafe-perm  
  
CMD npm start  

