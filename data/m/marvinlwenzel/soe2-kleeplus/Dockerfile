FROM klee/klee:latest  
  
#Labels  
LABEL description="Image inteneded to be used for Reykjavik University course
Sorftware Engineering 2 in 2017. \  
Is based on klee/klee:latest and adds useful packages for implementing testing
software."  
LABEL maintainer="marvin16@ru.is"  
#Adding packages  
USER root  
  
#Install JDK 8  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
  
#Setting up environmental variables for Java  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $PATH:$JAVA_HOME/bin  
  
#Install maven  
RUN apt-get install -y maven && \  
apt-get clean  
  
#Install llvm 3.3. Fix problem stated in piazza.  
RUN apt-get install -y llvm-3.3 && \  
apt-get clean  
  
  
#Go back to user klee so that one does not enter the Image as root  
USER klee  

