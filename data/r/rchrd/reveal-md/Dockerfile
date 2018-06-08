FROM alpine:3.4  
RUN apk add --no-cache nodejs  
  
RUN npm install -g reveal-md  
  
ADD custom.css /usr/lib/node_modules/reveal-
md/node_modules/reveal.js/css/theme/custom.css  
  
RUN mkdir -p /presentations  
WORKDIR /presentations  
  
EXPOSE 8000  
ENTRYPOINT ["reveal-md", "--port", "8000", "--disableAutoOpen", "--theme",
"custom"]  

