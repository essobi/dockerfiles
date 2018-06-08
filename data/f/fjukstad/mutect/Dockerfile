FROM fjukstad/gatk  
  
USER root  
  
RUN apt-get update && apt-get install -y \  
r-base  
  
# Install Java 1.7 (since MuTect for some reason does not work with 1.8)  
# RUN apt-get install -y software-properties-common  
# RUN add-apt-repository -y ppa:webupd8team/java  
# RUN apt-get update  
# RUN sudo mv jdk-7u(downloadedversion)-linux-x64.tar.gz /var/cache/oracle-
jdk7-installer/  
# RUN apt install -y oracle-java7-installer  
RUN apt-get install -y software-properties-common python-software-properties  
RUN apt install debian-archive-keyring  
RUN add-apt-repository 'deb http://httpredir.debian.org/debian experimental
main'  
RUN add-apt-repository 'deb http://httpredir.debian.org/debian sid main'  
COPY debian /etc/apt/preferences.c/debian  
RUN apt update  
RUN apt install -y openjdk-7-jdk  
RUN update-java-alternatives -s java-1.7.0-openjdk-amd64  
# RUN add-apt-repository ppa:openjdk-r/ppa  
# RUN apt-get update  
# RUN apt-get install openjdk-7-jdk  
WORKDIR /tools  
RUN mkdir mutect  
WORKDIR mutect  
COPY mutect-1.1.7.jar.zip mutect-1.1.7.jar.zip  
RUN unzip mutect-1.1.7.jar.zip  
  
USER worker  
ENTRYPOINT ["java", "-jar", "/tools/mutect/mutect-1.1.7.jar"]  

