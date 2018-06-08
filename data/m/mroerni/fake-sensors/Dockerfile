FROM clojure:lein-alpine  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
EXPOSE 3000  
CMD ["lein", "ring", "server-headless"]

