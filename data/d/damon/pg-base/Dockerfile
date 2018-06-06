# damon/pg-base  
#  
# This adds the postgres repository to the apt-get sources  
FROM damon/base  
  
# Add the postgresql repository  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list.d/postgres.list  
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
# Update the apt cache on build  
ONBUILD RUN apt-get update  

