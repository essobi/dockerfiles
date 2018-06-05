############################################################################  
# This dockerfile will setup a centos container with OpenJDK installed on it  
############################################################################  
  
FROM loicmathieu/openjdk  
  
MAINTAINER Loic Mathieu <loicmathieu@free.fr>  
  
ADD imq.tar /opt/imq.tar  
  
COPY imqenv.conf /opt/imq.tar/imq/etc  
  
EXPOSE 7676 1099  
  
VOLUME /var/imq  
VOLUME /opt/imq.tar/imq/etc  
  
ENTRYPOINT ["/opt/imq.tar/imq/bin/imqbrokerd", "-vmargs", "-d64", "-port",
"7676"]  

