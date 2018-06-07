FROM postgres:9.6.6-alpine  
MAINTAINER Siddhartha Basu<siddhartha-basu@northwestern.edu>  
  
# place for custom configuration files, no need to change  
RUN mkdir -p /etc/postgresql/conf.d  
COPY postgresql.conf /etc/postgresql/  
COPY [^p]*.conf /etc/postgresql/conf.d/  
COPY *.sh /docker-entrypoint-initdb.d/  
  
# Add env variables for example, to new users during initialization  
# Those can be used in the start up script(.sh files) to run against the
database  
ENV DICTYCONTENT_USER dictycontent  
ENV DICTYCONTENT_PASSWORD contentpass  
ENV DICTYCONTENT_DB dictycontent  
ENV DICTYUSER_USER dictyuser  
ENV DICTYUSER_PASSWORD userpass  
ENV DICTYUSER_DB dictyuser  

