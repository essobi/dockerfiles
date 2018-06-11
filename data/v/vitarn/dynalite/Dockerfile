FROM node:alpine  
  
WORKDIR /app  
  
ENV NODE_ENV production  
ENV DYNALITE_VERSION 1.2.0  
  
RUN apk add --no-cache --virtual .build-deps \  
python \  
make \  
g++ \  
&& npm install dynalite@$DYNALITE_VERSION --no-save \  
&& rm -Rf ~/.npm \  
&& find \\( \  
-type f \  
-name '.*ignore' -o \  
-name '.*rc' -o \  
-name '.travis.yml' -o \  
-name 'LICENSE*' -o \  
-name 'README*' -o \  
-name 'CHANGELOG*' -o \  
-name 'Makefile' -o \  
-name 'test.js' -o \  
-name 'example.js' -o \  
-name '*.test.js' -o \  
-name '*.ts' -o \  
-name 'yarn.lock' \  
\\) -delete \  
&& apk del .build-deps  
  
EXPOSE 4567  
  
CMD ["./node_modules/.bin/dynalite", "--createTableMs 0", "--deleteTableMs 0",
"--updateTableMs 0"]  

