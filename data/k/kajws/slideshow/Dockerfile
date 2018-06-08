FROM node:8  
  
WORKDIR /app  
COPY server/package.json server/package.json  
COPY server/yarn.lock server/yarn.lock  
  
RUN cd server && yarn install --frozen-lockfile  
  
COPY client client  
  
RUN cd client && yarn install --frozen-lockfile && yarn build && mv build
../server/public && cd /app && rm -Rf client  
  
COPY server server  
  
WORKDIR /app/server  
CMD ["yarn", "start"]

