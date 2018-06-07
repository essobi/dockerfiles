FROM java:8  
MAINTAINER Olivier Liechti <olivier.liechti@heig-vd.ch>  
  
#  
# When we build the image, we copy the executable jar in the image file
system.  
#  
COPY StreamingTimeServer-1.0-SNAPSHOT-standalone.jar /opt/app/server.jar  
  
#  
# Our application will accept TCP connections on port 2205. Note that the
EXPOSE statement  
# does not make the container accessible via the host. For the container to
really be accessible,  
# we must either use the -p or the -P flag when using the docker run command.
With -p, we can  
# specify an explicit port mapping (and EXPOSE is not even required). With -P,
we let Docker  
# assign random ports for each EXPOSEd port. We can then use the docker port
command to know the port  
# numbers that have been selected.  
#  
EXPOSE 2205  
#  
# This is the command that is executed when the Docker container starts  
#  
CMD ["java", "-jar", "/opt/app/server.jar"]

