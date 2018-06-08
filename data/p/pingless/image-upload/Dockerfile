FROM node:8  
ENV workdir /srv/  
# All our commands are now relative to the serve folder  
WORKDIR $workdir  
  
# Copy these files first, so that subsequent builds don't need to re-run the
yarn install step  
COPY ./package.json ./yarn.lock $workdir  
RUN yarn install  
  
# Copy the rest of the files  
COPY . $workdir  
  
RUN yarn run build  
  
EXPOSE 3000  
CMD ["yarn", "run", "start"]  

