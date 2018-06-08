FROM postgres:latest  
  
ENV POSTGRES_PASSWORD pact  
ENV POSTGRES_USER admin  
  
ADD config/setup.sql /docker-entrypoint-initdb.d

