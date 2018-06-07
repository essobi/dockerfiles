FROM node:9.11-alpine  
LABEL maintainer="Ahmad Nassri <ahmad@ahmadnassri.com>"  
LABEL greenlight.version="1.0.0"  
LABEL greenlight.name="greenlight/eslint"  
LABEL greenlight.description="A fully pluggable tool for identifying and
reporting on patterns in JavaScript"  
  
WORKDIR /app/  
  
COPY package.json /app/  
COPY package-lock.json /app/  
  
RUN npm i --prod  
  
COPY lib /app/lib  
COPY index.js /app/  
  
RUN chmod +x index.js  
  
VOLUME /source/  
WORKDIR /source/  
  
ENTRYPOINT ["/app/index.js"]  
CMD ["run"]  

