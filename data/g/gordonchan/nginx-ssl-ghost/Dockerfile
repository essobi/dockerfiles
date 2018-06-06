FROM nginx:latest  
MAINTAINER Gordon Chan <github.com/gchan>  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
ADD entrypoint.sh .  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

