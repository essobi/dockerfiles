FROM postgres  
MAINTAINER "Hiroki Takeyama"  
# timezone  
ENV TZ Asia/Tokyo  
  
# postgres info  
ENV POSTGRES_USER postgres  
ENV POSTGRES_PASSWORD postgres  
  
VOLUME /var/lib/postgresql/data  
  
EXPOSE 5432  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["postgres"]  

