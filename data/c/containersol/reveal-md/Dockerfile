FROM alpine:3.4  
  
WORKDIR /usr/src/app  
  
RUN apk update && apk add nodejs git  
RUN npm install -g webpro/reveal-md#2.0.0-rc.2  
  
RUN mkdir -p /usr/lib/node_modules/reveal-md/node_modules/reveal.js/images  
  
COPY resources/cs.png /usr/lib/node_modules/reveal-
md/node_modules/reveal.js/css/theme  
COPY resources/slide-background.svg /usr/lib/node_modules/reveal-
md/node_modules/reveal.js/css/theme/  
COPY resources/title-background.svg /usr/lib/node_modules/reveal-
md/node_modules/reveal.js/css/theme/  
COPY resources/cs.css /usr/lib/node_modules/reveal-
md/node_modules/reveal.js/css/theme/  
COPY resources/reveal.html /usr/lib/node_modules/reveal-md/lib/template/  
COPY resources/listing.html /usr/lib/node_modules/reveal-md/lib/template/  
  
EXPOSE 1948  
  
CMD ["sh", "-c", "reveal-md /usr/src/app -w --theme cs"]  

