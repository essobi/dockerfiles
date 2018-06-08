FROM docker:latest  
RUN apk update && apk add nodejs curl  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 \  
&& chmod +x /usr/local/bin/dumb-init  
COPY . /app  
WORKDIR /app/  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
CMD node index.js  
EXPOSE 80  

