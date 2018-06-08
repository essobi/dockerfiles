FROM malczuuu/angular-cli:6.0.1 as builder  
  
WORKDIR /ng-app  
  
ADD . .  
  
RUN yarn && ng build --prod --configuration=production  
  
FROM nginx:1.14-alpine  
  
## Remove default nginx website  
RUN rm -rf /usr/share/nginx/html/*  
  
COPY \--from=builder /ng-app/dist/* /usr/share/nginx/html/  
  
## Copy our default nginx config  
COPY nginx/default.conf /etc/nginx/conf.d/  
  
CMD nginx -g "daemon off;"  

