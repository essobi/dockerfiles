FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/app/resources  
RUN mkdir -p /usr/src/app/public  
WORKDIR /usr/src/app  
  
# Install deployd  
RUN npm install deployd@0.8.8  
  
# Copy source code  
COPY .dpd /usr/src/app/.dpd  
COPY app.dpd /usr/src/app/  
COPY resources /usr/src/app/resources/  
COPY run.js /usr/src/app/  
COPY public /usr/src/app/public/  
  
EXPOSE 3000  
CMD [ "node", "run.js" ]

