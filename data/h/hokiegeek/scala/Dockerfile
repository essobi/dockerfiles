FROM openjdk:jdk  
  
RUN mkdir /app  
VOLUME /app  
  
RUN wget http://downloads.lightbend.com/scala/2.12.1/scala-2.12.1.tgz  
  
RUN tar -xvzf scala-2.12.1.tgz  
RUN cp scala-2.12.1/bin/* /usr/bin  
RUN cp scala-2.12.1/lib/* /usr/lib  
  
RUN rm -rf scala-2.12.1*  
  
WORKDIR /app  

