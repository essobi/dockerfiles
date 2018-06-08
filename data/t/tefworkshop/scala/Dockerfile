FROM ubuntu  
  
MAINTAINER Stefan Hans <stefan.hans@telefonica.com>  
  
# Install Java  
RUN apt-get update && apt-get install openjdk-8-jdk -y  
RUN java -version  
  
# Install sbt  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
RUN apt-get install apt-transport-https -y  
RUN apt-get update  
RUN apt-get install sbt -y  
  
RUN sbt about  
  
# Scala  
ENV SCALA_HOME /home/Scala  
ENV SCALA_TEST /home/Scala/Test  
  
RUN mkdir ${SCALA_HOME} ${SCALA_TEST}  
RUN cd ${SCALA_TEST}  
  
RUN echo ":quit" | (sbt console)  
  
CMD ["/bin/bash"]  

