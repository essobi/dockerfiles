FROM nginx:mainline-alpine  
  
LABEL maintainer Oscar Barrett  
  
ARG version  
LABEL version $version  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN rm /etc/nginx/conf.d/default.conf  

