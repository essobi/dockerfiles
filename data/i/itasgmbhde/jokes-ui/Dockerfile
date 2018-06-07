# Angular App ========================================  
FROM node:10 as angular-app  
LABEL authors="Shayne Boyer, John Papa"  
RUN npm install -g @angular/cli  
# Copy and install the Angular app  
WORKDIR /app  
COPY package.json /app  
COPY . /app  
RUN npm install yarn && yarn install  
RUN mkdir -p /app/dist/publicweb && yarn run build --prod  
  
#Express server =======================================  
FROM node:10 as express-server  
RUN apt-get update \  
&& apt-get install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-
essential g++ libpng12-dev -y --no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /app  
COPY /src/server /app  
RUN npm install yarn  
RUN yarn install --production --silent  
  
#Final image ========================================  
FROM node:10  
RUN mkdir -p /usr/src/app  
RUN apt-get update \  
&& apt-get install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-
essential g++ libpng12-dev -y --no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /usr/src/app  
COPY \--from=express-server /app /usr/src/app  
COPY \--from=angular-app /app/dist /usr/src/app  
RUN mkdir -p /usr/src/app/dist && ln -s /usr/src/app/publicweb
/usr/src/app/dist/publicweb  
ENV PORT 80  
#ENV API_URL we-could-set-this-here-as-default  
CMD [ "node", "index.js" ]  

