FROM sitapati/docker-alpine-python-node  
  
# Install dependencies  
RUN apk add --update \  
build-base \  
python \  
&& npm install -g bower gulp \  
&& rm /var/cache/apk/*  
  
RUN apk add --no-cache bash git openssh  
  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN npm install  
  
RUN bower install --allow-root  
CMD ["npm","test"]  

