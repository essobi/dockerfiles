FROM pablozaiden/typescript:docker  
  
ONBUILD COPY . /app  
ONBUILD RUN yarn install  
ONBUILD RUN tsc -p .  

