# docker build -t romach007/gradle:1.0.0 -t romach007/gradle:latest .  
# docker run -id --name gradle romach007/gradle  
# docker exec -u user -it gradle /bin/bash  
FROM romach007/java8:latest  
LABEL maintainer="romach007@gmail.com"  
  
USER user  
WORKDIR /home/user  
  
# download Gradle archive  
RUN wget -O ~/gradle-4.2.1-bin.zip
https://services.gradle.org/distributions/gradle-4.2.1-bin.zip  
  
# install unzip - tool for extracting compressed files from ZIP archive:  
RUN sudo apt-get install unzip  
  
# unzip Gradle archive:  
RUN sudo mkdir /opt/gradle  
RUN sudo unzip -d /opt/gradle ~/gradle-4.2.1-bin.zip  
  
# delete Gradle archive:  
RUN rm ~/gradle-4.2.1-bin.zip  
  
# add Gradle to `PATH` environment variable:  
RUN echo "export PATH=\$PATH:/opt/gradle/gradle-4.2.1/bin" >> ~/.bashrc

