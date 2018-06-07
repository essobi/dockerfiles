FROM node:argon  
  
WORKDIR /home/feathers  
COPY README.md README.md  
COPY package.json package.json  
COPY config/ config/  
COPY public/ public/  
COPY src/ src/  
ENV NODE_ENV 'production'  
ENV PORT '8080'  
ENV NEDB_BASE_PATH '../data'  
ENV SECRET 'lots and lots of secrets'  
ENV GITHUB_CLIENT_ID 'client id'  
ENV GITHUB_CLIENT_SECRET 'client secret'  
RUN npm install --production  
CMD [ "node", "src/index.js" ]

