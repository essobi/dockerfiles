FROM node AS build-env  
COPY . /root  
WORKDIR /root  
RUN npm install  
RUN npm run build  
  
FROM nginx  
  
EXPOSE 443  
ENV API_HOST api  
ENV API_PORT 4444  
COPY \--from=build-env /root/dist/ /var/html/  
COPY nginx.conf /etc/nginx/  
COPY entrypoint.sh /root  
CMD ["nginx"]  
  

