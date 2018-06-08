from iojs:slim  
  
workdir /app  
add package.json /app/  
add node_modules /app/node_modules  
run npm install  
add . /app  
  
run mkdir -p dist  
run node_modules/.bin/babel index.js > dist/index.js  
  
expose 3000  
cmd ["node", "dist/index.js"]  

