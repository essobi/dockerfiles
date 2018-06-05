FROM docker/compose:1.8.0  
ENTRYPOINT ["/entrypoint"]  
  
# Default config for where to store the project name  
ENV PROJECT_NAME_FILE ".compose-project-name"  
ENV DB=false  
ENV PORT=8000  
ENV DJANGO_DEBUG=true  
ENV WATCH=true  
  
ADD docker-compose.db.yml /docker-compose.db.yml  
ADD docker-compose.yml /docker-compose.yml  
ADD common.yml /common.yml  
ADD entrypoint /entrypoint  
ADD USAGE.md /USAGE.md  
ADD bin /bin/  

