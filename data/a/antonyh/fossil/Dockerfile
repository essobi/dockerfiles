###  
# Dockerfile for Fossil  
#  
# Although it works fine, there is a one little thing which is not 100%  
# correct: the fossil repository is created at Docker image creation time,  
# which means everyone using the same docker image will have the same  
# server ID and project ID.  
#  
# This is a fork of nijtmans/fossil, changed to use ubuntu & apt-get  
# The fossil commands have also been changed to work with v1.27  
#  
###  
FROM ubuntu  
RUN apt-get update -y && apt-get clean all  
  
RUN mkdir /data  
RUN apt-get install -y fossil && apt-get clean all  
RUN groupadd -r fossil -g 433 && useradd -u 431 -r -g fossil -d /data -s
/sbin/nologin -c "Fossil user" fossil  
RUN chown -R fossil:fossil /data  
  
USER fossil  
WORKDIR /data  
ENV HOME /data  
  
RUN fossil new -A admin /data/fossil.fossil  
RUN fossil user password -R /data/fossil.fossil admin admin  
#RUN fossil cache init -R /data/fossil.fossil  
  
EXPOSE 8080  
VOLUME ["/data"]  
CMD ["/usr/bin/fossil", "server", "/data/fossil.fossil"]  
  

