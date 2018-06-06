FROM postgres:9.6.1  
  
ENV POSTGRES_DB=ems_ecommerce  
ENV POSTGRES_USER=ems_ecommerce  
ENV POSTGRES_PASSWORD=ems_ecommerce  
  
RUN apt-get update -qq && \  
apt-get install -y apt-utils postgresql-contrib  
  
ADD *.sql /docker-entrypoint-initdb.d/  

