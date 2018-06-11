FROM nginx  
  
RUN mkdir -p /logs  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
ENV JENKINS_OPTS --prefix=/jenkins  
EXPOSE 80  

