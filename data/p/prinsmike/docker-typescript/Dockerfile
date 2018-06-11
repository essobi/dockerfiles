FROM node:alpine  
MAINTAINER Michael Prinsloo <mike.prinsloo@gmail.com>  
  
RUN apk add --no-cache --virtual .persistent-deps \  
curl \  
openssl \  
git \  
openssh \  
make \  
gcc \  
g++ \  
python \  
py-pip && \  
npm install --silent --save-dev -g \  
gulp-cli \  
typescript \  
webpack \  
create-react-app  
  
# Set up the application directory.  
VOLUME ["/app"]  
WORKDIR /app  
  
CMD ["npm", "-v"]  

