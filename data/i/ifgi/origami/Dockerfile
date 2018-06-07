FROM monostream/nodejs-gulp-bower  
  
# Setup build folder  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN npm install  
  
RUN gulp build  
  
VOLUME /usr/src/app  
  
COPY ./run.sh /  
  
CMD ["./run.sh"]

