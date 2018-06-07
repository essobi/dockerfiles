FROM mhart/alpine-node  
# docker run -it mhart/alpine-node /bin/sh  
# docker run -it -v $PWD:/delegito mhart/alpine-node /bin/sh  
#FROM nginx:alpine - if I wasn't compiling JS/CSS/html  
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"  
RUN apk --update add supervisor nginx git  
RUN npm install -g bower eslint uglifyjs jasmine js-beautify eslint-plugin-es-
beautifier eslint-plugin-react  
COPY conf/ /deploy/  
RUN nginx -t -c /deploy/nginx.conf  
COPY package.json /srv/package.json  
WORKDIR /srv/  
RUN npm install  
  
COPY src/ /srv/  
# not using grunt or gulp. Too annoying right now.  
RUN find js -type f -name "*.js" -exec js-beautify --config beauty.json {} -r
\; && \  
eslint --config lint.json --fix js/ && \  
find js -name "*.js" -exec cat {} >> concat.js \; && \  
uglifyjs concat.js -o final.js && \  
bower install --allow-root && \  
rm -r bower.json package.json node_modules gulpfile.js  
EXPOSE 80  
CMD ["supervisord","-c","/deploy/supervisord.conf"]  

