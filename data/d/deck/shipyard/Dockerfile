FROM debian:jessie  
COPY . /app  
RUN apt-get update && apt-get install golang git mercurial nodejs npm -y &&
npm install -g bower && export GOPATH=/app && cd /app && go get . ; go build .
&& mv /app/app /app/controller && cd /app/static && ln -s /usr/bin/js
/usr/bin/node && bower --allow-root install  
EXPOSE 8080  
ENTRYPOINT ["/app/controller"]  

