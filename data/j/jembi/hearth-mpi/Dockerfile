FROM nginx  
  
WORKDIR /src/frontend/  
  
# Update apt-repo list and install prerequisits  
RUN apt-get update  
RUN apt-get install -y bzip2  
RUN apt-get install -y curl gnupg gnupg2 gnupg1  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
RUN node -v  
RUN npm -v  
  
# Add package.json to image and install dependencies  
ADD package-lock.json /src/frontend/  
ADD package.json /src/frontend/  
RUN npm install  
  
# Add scripts and views to image  
ADD . /src/frontend/  
  
# build script bundle  
RUN npm run build  
  
# copy bundles and scripts to nginx host folder  
RUN mv dist/ /usr/share/nginx/html  
RUN mv app/ /usr/share/nginx/html  
RUN mv node_modules/ /usr/share/nginx/html  
RUN mv index.html /usr/share/nginx/html  

