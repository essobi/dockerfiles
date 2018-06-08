From ubuntu:14.04  
RUN apt-get update && apt-get install -y wget  
  
RUN apt-get update && apt-get install -y openjdk-7-jre  
  
RUN wget http://www.scala-lang.org/files/archive/scala-2.11.4.deb  
RUN dpkg -i scala-2.11.4.deb  
RUN apt-get update && apt-get install -y scala  
  
WORKDIR /root  
  
RUN wget http://dl.bintray.com/sbt/debian/sbt-0.13.6.deb  
RUN dpkg -i sbt-0.13.6.deb  
RUN apt-get update && apt-get install -y sbt  
  
#ADD skinny-blank-app-with-deps.zip ./  
RUN wget https://github.com/skinny-framework/skinny-
framework/releases/download/1.3.16/skinny-blank-app-with-deps.zip  
RUN apt-get update && apt-get install -y unzip  
RUN unzip skinny-blank-app-with-deps.zip  
WORKDIR /root/skinny-blank-app  
EXPOSE 8080  
ENTRYPOINT ["./skinny","run"]  

