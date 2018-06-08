FROM node:8.2.1  
WORKDIR app  
  
# Run npm install first for nice caching  
ADD package.json package.json  
# FIXME: think about this one, could just install the prod deps, but what  
# about typescript transpiling? where to handle that then?  
RUN npm install  
  
ADD . .  
  
EXPOSE 6660  
CMD ["npm", "start"]

