FROM postgres:9.3  
ENV PG_MAJOR 9.3  
RUN apt-get update \  
&& apt-get install -y postgresql-$PG_MAJOR-plr \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

