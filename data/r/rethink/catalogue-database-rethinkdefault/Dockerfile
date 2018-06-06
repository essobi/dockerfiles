FROM rethink/catalogue-database  
MAINTAINER marc.emmelmann@fokus.fraunhofer.de  
  
#  
# Attention: run with  
#  
# docker run -it --net=host  
#  
# just assure that the database and default objects are installed.  
RUN cd /opt/reTHINK/catalogue/;mkdir catalogue_objects; cd
/opt/reTHINK/catalogue/catalogue_objects  
  
# copy your own catalogue objects (as contained below the directory, this  
# docker file resides in) onto the docker image  
COPY catalogue_objects/ /opt/reTHINK/catalogue/catalogue_objects/  
  
# ENTRYPOINT is the command that is always run.  
# ENTRYPOINT ["java", "-jar",
"/opt/reTHINK/catalogue/catalogue_database/target/rethink-catalogue-database-
jar-with-dependencies.jar", "-o", "/opt/reTHINK/catalogue/catalogue_objects"]  

