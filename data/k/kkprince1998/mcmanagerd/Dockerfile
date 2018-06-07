FROM kkprince1998/dockeroraclejava  
  
RUN mkdir /tmp/mvn -p;cd /tmp/mvn; \  
wget -O -
http://apachemirror.ovidiudan.com/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar xz; \  
mv * /tmp/maven  
RUN cd /  
  
RUN mkdir -p /work /mcManagerd  
ADD . /work/  
  
RUN cd /work/; /tmp/maven/bin/mvn clean compile package  
RUN echo "mv $(find /work/target | grep "jar-with-dependencies\\.jar$")
/mcManagerd/mcManagerd.jar" | bash  
  
RUN rm -rf work  
  
WORKDIR /mcManagerd  
CMD ["java", "-jar", "mcManagerd.jar"]

