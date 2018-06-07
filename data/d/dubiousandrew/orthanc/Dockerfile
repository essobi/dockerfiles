#Run this image with: docker run -p 8042:8042 -v  
#FROM ubuntu also works the same, but only has orthanc v1.0, debian has v1.2,
and fedora doesnt work  
FROM debian  
#install orthanc  
RUN apt-get upgrade && apt-get update && apt-get install -y orthanc  
#copy the local orthanc settings  
#COPY orthanc.json /etc/orthanc/orthanc.json  
#persist the sqlite and storage, this matches the settings in the orthanc.json
file  
#VOLUME [ "/var/lib/orthanc/db-v6" ]  
#EXPOSE 4242 not used for now  
EXPOSE 8042  
ENTRYPOINT [ "Orthanc", "/etc/orthanc/orthanc.json"]

