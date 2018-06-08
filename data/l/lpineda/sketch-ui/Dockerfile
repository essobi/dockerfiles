# build environment  
FROM node:9.5 as builder  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
ENV PATH /usr/src/app/node_modules/.bin:$PATH  
ADD package.json /usr/src/app/package.json  
RUN npm install --silent  
RUN npm install react-scripts@1.1.1 -g --silent  
RUN npm install cors  
RUN npm install react-vis --save  
RUN npm install react-bootstrap-table-next --save  
  
ADD . /usr/src/app  
RUN npm run build  
  
# production environment  
FROM nginx:1.13.5-alpine  
COPY \--from=builder /usr/src/app/build /usr/share/nginx/html  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

