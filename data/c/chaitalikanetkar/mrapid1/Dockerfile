#FROM ubuntu:12.04  
FROM java  
MAINTAINER Chaitali Kanetkar  
  
WORKDIR /mRapidMFToHadoop  
#RUN apt-get update && \  
#apt-get -y install sudo  
#RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  
# Copy the pom.xml into the container to install all dependencies  
COPY pom.xml ./  
  
# Copy the whole repository into the container  
COPY . ./  
  
#You could use volumes to put a file in the container in runtime  
VOLUME /Jar  
  
#In the Dockerfile, add a local file using ADD  
ADD mRapidMFToHadoop-0.0.1-SNAPSHOT.jar /mRapid.jar  
ADD mf_ebcdic_data_file1.txt /  
ADD cpybook_mf_ebcdic_data.txt /  
ADD mf.txt /  
#COPY mRapid.jar /  
EXPOSE 4567  
#ENTRYPOINT ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar",
"mRapidMFToHadoop-0.0.1-SNAPSHOT.jar"]  
#RUN bash -c 'touch /mRapid.jar'  
ENTRYPOINT ["java", "-jar", "/mRapid.jar"]  
#CMD "echo" "Hello, docker conatiner is created!"  
CMD ["/cpybook_mf_ebcdic_data.txt","/mf_ebcdic_data_file1.txt","/mf.txt"]

