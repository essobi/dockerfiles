FROM java:8  
MAINTAINER roadster <lizard43@gmail.com>  
  
ENV OWF_FILE OWF-bundle-7.17.0.tar.gz  
  
RUN apt-get update  
  
# github limits files to be 100MB so the OWF tarball  
# has been split in 3 pieces and then re-assembled in the image.  
COPY split/ /tmp/OWF/.  
RUN cat /tmp/OWF/OWF* > /tmp/OWF/$OWF_FILE && \  
mkdir /OWF && \  
cd /OWF && \  
tar -zxvf /tmp/OWF/$OWF_FILE . && \  
rm -fr /tmp/OWF  
  
EXPOSE 8080  
EXPOSE 8443  
WORKDIR /OWF/apache-tomcat  
  
CMD ["./start.sh"]  
  
# browse to http://localhost:8080/owf  
# Username/Password: testAdmin1/password

