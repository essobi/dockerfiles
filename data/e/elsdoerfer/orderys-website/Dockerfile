FROM node:8-onbuild  
ENV PORT 8080  
EXPOSE 8080  
  
RUN yarn  
RUN yarn run build  
  
  
CMD ["npm", "run", "serve"]  

