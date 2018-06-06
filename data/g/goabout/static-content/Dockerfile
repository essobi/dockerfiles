FROM nginx  
  
MAINTAINER joost@cassee.net  
  
ENV CONTENT="<!-- empty -->"  
ADD nginx.conf /etc/nginx/conf.d/default.conf  
  
ADD start.sh /usr/local/bin/start  
RUN chmod +x /usr/local/bin/start  
  
ENTRYPOINT ["start"]  
CMD ["nginx", "-g", "daemon off;"]  

