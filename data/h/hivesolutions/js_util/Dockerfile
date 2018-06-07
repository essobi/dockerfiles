FROM hivesolutions/python:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 8080  
ENV LEVEL INFO  
ENV ENCODING gzip  
ENV HOST 0.0.0.0  
ENV PORT 8080  
ENV CACHE 86400  
ENV INDEX_FILES index.html  
ENV CORS 1  
ENV BASE_PATH /docs/gen  
  
ADD package.json /  
ADD gulpfile.js /  
ADD README.md /  
ADD lib /lib  
  
RUN apk update && apk add nodejs  
RUN pip3 install --upgrade netius  
RUN npm install  
RUN npm install --only=dev  
RUN npm run docs  
  
CMD ["/usr/bin/python3", "-m", "netius.extra.filea"]  

