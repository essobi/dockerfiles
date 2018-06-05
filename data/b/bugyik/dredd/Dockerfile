FROM node:9.11-alpine  
MAINTAINER Petr Bugyík  
  
RUN apk add --no-cache --virtual .build-dependencies \  
make \  
gcc \  
g++ \  
python \  
git \  
&& \  
npm install dredd@"~5.1" && \  
apk del .build-dependencies && \  
npm cache --force clean && \  
rm -rf node_modules/faker && \  
find node_modules \  
-not \\( -path node_modules/chai/lib -prune \\) \  
-not \\( -path node_modules/rx -prune \\) \  
-not \\( -path node_modules/dredd-transactions -prune \\) \  
\\( \\( -iname "readme*" -or -iname "changelog*" -or -iname "test*.js" -or
-iname "*.min.js" \\) -and -type f \\) -or \  
\\( \\( -iname "dist" -or -iname "min" -or -iname "test*" -or -iname "doc*"
-or -iname "example*" -or -iname "build" -or -iname "benchmark*" \\) -and
-type d \\) \  
| xargs rm -rf  
  
ENTRYPOINT ["/node_modules/.bin/dredd"]  

