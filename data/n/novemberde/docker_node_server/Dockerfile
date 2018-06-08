FROM novemberde/node-pm2  
  
MAINTAINER KH BYUN "novemberde.github.io"  
# RUN npm install -g pm2 node-gyp  
ENV NODE_ENV production  
ENV PORT 80  
EXPOSE 80  
COPY ./ /src  
  
RUN npm install --prefix /src  
  
CMD ["pm2-docker", "/src/app.js"]

