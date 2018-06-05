FROM mongo  
MAINTAINER @thomasjmoerman  
ENV REFRESHED_AT 2016-04-15  
RUN apt-get update && apt-get upgrade -y  
EXPOSE 27017  
EXPOSE 28017  
ADD beers.json /startup/beers.json  
ADD import-student-db.sh /startup/import-student-db.sh  
ADD docker-startup.sh /startup/docker-startup.sh  
ADD students_2016.txt /startup/students.txt  
  
RUN mkdir ~/mongo  
  
# make script executable  
RUN chmod a+x /startup/docker-startup.sh  
RUN chmod a+x /startup/import-student-db.sh  
  
CMD ["/bin/sh", "/startup/docker-startup.sh"]

