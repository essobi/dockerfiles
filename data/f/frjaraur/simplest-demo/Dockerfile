FROM alpine  
RUN apk --update --update --no-progress --no-cache add nodejs  
ENV APPDIR /APP  
  
WORKDIR ${APPDIR}  
  
COPY simplestapp.js simplestapp.js  
COPY simplestapp.html simplestapp.html  
COPY package.json package.json  
COPY dbconfig.json dbconfig.json  
RUN npm install  
#DEFAULT PORT 3000  
CMD ["node","simplestapp.js","3000"]  
EXPOSE 3000  

