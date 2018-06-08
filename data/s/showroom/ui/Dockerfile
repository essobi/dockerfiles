FROM node:0.10-onbuild  
ENV NODE_ENV production  
RUN bash -c "node_modules/node-sass/bin/node-sass --output-style compressed
static/src/scss/app.scss static/src/scss/app.css"  
RUN bash -c "node_modules/browserify/bin/cmd.js -t reactify
static/src/js/app.js -o static/bundle.js"  
RUN bash -c "node_modules/jsmin/bin/jsmin static/bundle.js >
static/bundle.min.js"  
EXPOSE 8888  

