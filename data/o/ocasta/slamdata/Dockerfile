FROM openjdk:8  
MAINTAINER "Ocasta Studios <info@ocasta.com>"  
RUN wget -q -O slamdata.tar.bz2 https://s3.amazonaws.com/slamdata-
installers/4.2.6/slamdata-advanced_4_2_6.tar.bz2 && \  
tar xvjf slamdata.tar.bz2; rm slamdata.tar.bz2  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
CMD . /run.sh  

