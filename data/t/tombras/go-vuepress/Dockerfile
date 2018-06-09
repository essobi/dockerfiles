FROM node:8 AS docs  
RUN npm i vuepress  
  
FROM golang:1.10  
RUN mkdir /node_modules  
COPY \--from=docs /node_modules/ /node_modules  
COPY \--from=docs /usr/local/bin/node /usr/local/bin/node  
ENV PATH="/node_modules/.bin:${PATH}"  
RUN go get -u github.com/gobuffalo/packr/...  
RUN go get github.com/Microsoft/go-winio  
RUN go get golang.org/x/sys/windows

