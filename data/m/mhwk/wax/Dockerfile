FROM node:8  
WORKDIR /wax  
COPY ./ /wax  
RUN yarn install && yarn run build && rm -Rf node_modules ~/.npm  
  
FROM nginx:alpine  
WORKDIR /wax  
  
COPY \--from=0 /wax/dist /wax/dist  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
# HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://127.0.0.1/ ||
exit 1  
EXPOSE 80  

