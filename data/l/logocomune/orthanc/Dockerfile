# Fedora 21  
FROM fedora:21  
# Install deltarpm  
RUN yum -y install deltarpm  
  
# Update fedora  
RUN yum -y update  
  
# Install Orthanc  
RUN yum -y install orthanc  
  
# Add custom orthanc.json configuration file  
ADD orthanc.json /etc/orthanc/orthanc.json  
  
# Should be the same of "StorageDirectory" and "IndexDirectory" into
orthanc.json  
VOLUME ["/var/lib/orthanc/db-v5"]  
  
# docker exec -i .... bash  
# https://github.com/dockerfile/mariadb/issues/3  
ENV TERM dumb  
  
# Expose ports  
EXPOSE 8042  
EXPOSE 4242  
# Run Orthanc  
WORKDIR /  
ENTRYPOINT ["Orthanc"]  
# Orthanc configuration file def. position  
CMD ["/etc/orthanc/orthanc.json"]  

