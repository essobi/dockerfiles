FROM mhart/alpine-node:6  
COPY ./app /app  
  
WORKDIR /app  
  
RUN npm install  
  
ENV PORT=8080  
EXPOSE 8080  
ENTRYPOINT [ "node", "index.js" ]

