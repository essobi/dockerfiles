FROM mhart/alpine-node:6.7  
RUN apk add --update \  
git \  
make \  
gcc \  
libpng-dev \  
autoconf \  
automake \  
make \  
g++ \  
libtool \  
nasm  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY package.json /app  
RUN npm install --silent --production  
  
COPY . /app  
  
ENV NODE_ENV production  
  
CMD ["npm", "start"]  
  

