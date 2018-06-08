# First Stage  
FROM shito/alpine-node-gulp  
  
COPY . /usr/share/nginx/html  
  
RUN npm install  
RUN gulp build  
  
# Second Stage  
FROM nginx  
#FROM ewoutp/docker-nginx-curl  
COPY \--from=0 /usr/share/nginx/html/dist /usr/share/nginx/html/  
  
#HEALTHCHECK CMD curl -f http://localhost/ || exit 1  
EXPOSE 80

