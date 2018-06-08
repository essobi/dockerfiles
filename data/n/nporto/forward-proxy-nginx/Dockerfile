FROM nginx:1.11.1  
MAINTAINER Nick Portokallidis <portokallidis@gmail.com>  
  
WORKDIR /usr/share/nginx/html  
COPY . ./  
  
ENV PORT 80  
RUN rm /etc/nginx/conf.d/*.conf && mv /usr/share/nginx/html/nginx.conf.default
/etc/nginx/conf.d/nginx.conf  
  
EXPOSE 80  
CMD ["bash","run.sh"]

