FROM maven:3-jdk-8  
WORKDIR /root  
  
#Add Necessary Files and Environment settings  
# RUN wget https://bitbucket.org/findmyrun/findmyrun-
backend/raw/d3fdb6d2e25d69777d85822727235b05465c3f9c/pom.xml  
ADD pom.xml /root/pom.xml  
  
RUN mvn dependency:go-offline clean  
  
#Expose Rest Service Port  
EXPOSE 24244  
ENTRYPOINT ["/bin/bash"]

