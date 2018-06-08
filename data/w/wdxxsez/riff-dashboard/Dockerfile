FROM node:8.9.4-alpine  
  
RUN apk --update add git openssh && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
RUN git clone https://github.com/projectriff/dashboard  
  
WORKDIR dashboard  
RUN npm install --development  
RUN PUBLIC_URL=. npm run build  
CMD ["/dashboard/node_modules/.bin/serve", "--ssl", "build"]  

