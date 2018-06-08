FROM openjdk  
COPY . /var/www/java  
WORKDIR /var/www/java  
  
# COPY HelloWorld.jar HelloWorld.jar  
RUN javac Hello.java  
# RUN echo "Hello docker"  
# RUN java -jar HelloWorld.jar  
# RUN javac MountainBike.java  
# RUN javac Example.java  
CMD ["java", "Hello"]  
# CMD ["java", "Example"]  
# CMD ["java", "HelloWorld"]  
#CMD ["java", "MountainBike"]  
# CMD java -jar HelloWorld.jar  

