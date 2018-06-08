FROM manicmonkey/jdk:8  
MAINTAINER James Baxter <j.w.baxter@gmail.com>  
  
# Download youtrack  
WORKDIR /opt  
RUN apt-get update -q && apt-get install wget -qqy  
RUN wget -O youtrack.jar
https://download.jetbrains.com/charisma/youtrack-7.0.27965.jar  
  
VOLUME ["/data"]  
EXPOSE 8080  
CMD ["java", "-Xmx1g", "-Djava.awt.headless=true",
"-Ddatabase.location=/data", "-jar", "youtrack.jar", "8080"]  

