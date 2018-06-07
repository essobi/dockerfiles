FROM mhart/alpine-node:4.4  
RUN mkdir /app  
COPY ./app/package.json /app/package.json  
WORKDIR /app  
RUN npm install  
ADD . /  
ENTRYPOINT ["/app/runserver.sh"]  

