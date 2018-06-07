FROM nginx:latest  
LABEL mainteiner "jsaavedra@octobot.io"  
# 800X is the port for backend services  
# 300X is the port for browsersync for appX  
# 900X is the port for appX frontend  
# 600X is the port for livereload for appX  
  
EXPOSE 8000 8001 8443 8444 3000-3002 6000-6002 9000-9002  
COPY *.conf /etc/nginx/conf.availables/  
  
# END DockerfileBase  
  
RUN ln -s /etc/nginx/conf.availables/backend01.conf
/etc/nginx/conf.d/backend01.conf && \  
ln -s /etc/nginx/conf.availables/backend02.conf
/etc/nginx/conf.d/backend02.conf  

