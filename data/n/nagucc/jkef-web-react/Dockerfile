FROM node  
  
ADD *.js /jkef/  
ADD *.json /jkef/  
ADD .babelrc /jkef/  
ADD src /jkef/src  
ADD static /jkef/static  
ADD tools /jkef/tools  
ADD lib /jkef/lib  
WORKDIR /jkef  
  
RUN npm install  
RUN ./node_modules/.bin/babel-node tools/run build --release  
EXPOSE 5000  
RUN ls build  
CMD node build/server.js  

