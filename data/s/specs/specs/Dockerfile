FROM node:6.9.2  
ENV NODE_ENV production  
ENV SPECS_ALLOW_INSECURE_SSL false  
ENV SPECS_EXCLUDED_PATHS false  
  
WORKDIR /app  
  
ADD . /app  
  
RUN mkdir -p /app/project-data && useradd -d /app specs && chown -R
specs:specs /app  
  
VOLUME /app/project-data  
  
USER specs  
  
RUN npm install  
  
EXPOSE 3000  
CMD npm start  

