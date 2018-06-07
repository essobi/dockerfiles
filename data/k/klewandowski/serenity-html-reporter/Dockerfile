FROM anapsix/alpine-java  
  
RUN apk add --update nodejs  
  
RUN mkdir /app  
COPY . /app  
WORKDIR /app  
  
RUN npm install && \  
npm run pretest  
  
VOLUME ["/app/source", "/app/dest"]  
  
#CMD ["npm", "run", "report"]  
ENTRYPOINT ["npm"]  
CMD ["run", "report"]  

