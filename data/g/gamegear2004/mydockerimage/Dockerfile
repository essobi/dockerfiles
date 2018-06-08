FROM gamegear2004/mydockerimage:latest  
MAINTAINER darius korzeniewski (Darius_Korzeniewski@web.de)  
  
#Arbeitsbereich festlegen  
WORKDIR /home/  
  
# Ubuntu auf den aktuellen Stand bringen  
RUN apt-get autoremove -y  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get autoclean -y  
RUN apt-get install -y build-essential  
RUN apt-get install wget -y  
RUN apt-get install libcurl4-gnutls-dev -y  
  
# Terminal Editor Vim installieren  
RUN apt-get install vim -y  
  
# Swift nach installieren  
RUN apt-get install clang libicu-dev -y  
RUN wget https://swift.org/builds/development/ubuntu1404/swift-DEVELOPMENT-
SNAPSHOT-2016-02-25-a/swift-DEVELOPMENT-
SNAPSHOT-2016-02-25-a-ubuntu14.04.tar.gz  
RUN tar xzf swift-DEVELOPMENT-SNAPSHOT-2016-02-25-a-ubuntu14.04.tar.gz  
RUN export PATH=$(pwd)/swift-DEVELOPMENT-
SNAPSHOT-2016-02-25-a-ubuntu14.04/usr/bin/:"${PATH}"  

