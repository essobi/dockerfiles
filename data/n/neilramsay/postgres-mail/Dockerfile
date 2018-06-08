FROM postgres:alpine  
  
# Inherited from Postgres  
#ENTRYPOINT ['docker-entrypoint.sh']  
#CMD ['postgres']  
#EXPOSE 5432/tcp  
#VOLUME ["/var/lib/postgresql/data"]  
RUN apk add --no-cache gettext  
  
COPY conf /docker-entrypoint-initdb.d/  
  
ENV POSTGRES_DB=mail  
  
# Added for 'cleaner' image  
CMD ["postgres"]  

