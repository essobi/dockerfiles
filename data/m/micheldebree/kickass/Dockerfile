FROM openjdk:8-jre-alpine  
LABEL maintainer="michel@micheldebree.nl"  
ADD http://www.theweb.dk/KickAssembler/KickAssembler.zip /  
RUN unzip /KickAssembler.zip && rm /KickAssembler.zip  
WORKDIR /workspace  
ENTRYPOINT ["java","-jar","/KickAss.jar"]  

