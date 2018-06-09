FROM guligo/jdk-maven-ant-tomcat-mysql:latest  
  
#####  
# Git  
#####  
  
RUN apt-get update  
RUN apt-get install -y git  
  
##############  
# Tipspromenad  
##############  
  
WORKDIR /tmp  
ADD start.sh start.sh  
RUN chmod +x start.sh  
  

