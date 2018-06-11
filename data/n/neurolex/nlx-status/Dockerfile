FROM neurolex/nlx-base  
WORKDIR /usr/src/app  
ADD . /usr/src/app  
  
# install dependencies  
RUN npm install  
  
# run tests  
RUN npm test  
  
# expose and env  
ENV PORT 8080  
ENV HEALTH_CHECK 5000  
ENV NLX_COLLECTOR "http://nlx-collector-service:8080"  
EXPOSE 8080  
CMD ["node", "/usr/src/app/lib/index.js"]

