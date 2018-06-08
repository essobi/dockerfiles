FROM mhart/alpine-node:7  
MAINTAINER miaou  
  
RUN cd $(npm root -g)/npm && npm install fs-extra && sed -i -e s/graceful-
fs/fs-extra/ -e s/fs.rename/fs.move/ ./lib/utils/rename.js  
RUN cd  
  
# Create app directory  
RUN mkdir -p /app  
COPY . /app  
  
# Expose the app port  
EXPOSE 3000  
# Copy files.  
ONBUILD COPY . /app  
ONBUILD WORKDIR /app  
ONBUILD RUN npm install  
ONBUILD RUN ./node_modules/.bin/nuxt build  
  
CMD ["/app/run.sh"]  

