FROM openjdk:8-jre  
  
RUN apt-get update &&\  
apt-get install unzip &&\  
mkdir /usr/trimmomatic &&\  
cd /usr/trimmomatic &&\  
wget
'http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip'
&&\  
unzip Trimmomatic-0.36.zip  
  
ENV trimmomatic=/usr/trimmomatic/Trimmomatic-0.36/trimmomatic-0.36.jar  
ENV adapters=/usr/trimmomatic/Trimmomatic-0.36/adapters  

