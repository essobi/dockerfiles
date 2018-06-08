FROM ubuntu:latest  
  
MAINTAINER Piotr Kluch <206799@edu.p.lodz.pl>  
  
RUN apt-get update \  
\  
&& apt-get install -y openjdk-8-jdk scala wget git \  
\  
&& wget https://bintray.com/artifact/download/sbt/debian/sbt-0.13.8.deb \  
&& dpkg -i sbt-0.13.8.deb \  
\  
&& git clone https://github.com/piotrkluch/reactive-university-project.git
/app \  
&& cd /app \  
\  
&& sbt compile \  
&& sbt test \  
\  
&& apt-get remove -y wget git \  
&& apt-get clean \  
&& apt-get purge \  
&& rm /sbt-0.13.8.deb  
  
WORKDIR /app  
  
CMD ["sbt", "run"]  

