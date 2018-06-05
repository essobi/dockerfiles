FROM java:8  
RUN wget --progress=dot:mega
"https://dma.ci.cloudbees.com/job/AisWeb/lastSuccessfulBuild/artifact/target/ais-
web-0.1-SNAPSHOT-standalone.war" -O /ais-web.war  
WORKDIR /archive/  
EXPOSE 8080  
CMD ["java", "-jar", "/ais-web.war"]  

