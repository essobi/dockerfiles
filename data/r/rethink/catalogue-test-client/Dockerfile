FROM rethink/catalogue-database  
MAINTAINER vitor-t-silva@telecom.pt  
  
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

