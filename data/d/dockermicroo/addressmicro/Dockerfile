FROM java:openjdk-8u45-jdk  
  
MAINTAINER senthil@me.com  
  
RUN apt-get update -qq && apt-get install -y wget git  
  
RUN wget
http://mirror.fibergrid.in/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz && \  
tar -zxf apache-maven-3.3.9-bin.tar.gz && rm apache-maven-3.3.9-bin.tar.gz &&
\  
mv apache-maven-3.3.9 /usr/local && ln -s /usr/local/apache-
maven-3.3.9/bin/mvn /usr/bin/mvn  
  
RUN mkdir /app  
  
WORKDIR /app  
  
ADD . /app  
  
RUN mvn clean package -Pdeploy  
  
ENV JAVA_ENV=PRODUCTION  
  
EXPOSE 8080  
CMD ["java", "-server", "-cp", "target/classes:target/dependency/*",
"com.kumuluz.ee.EeApplication"]  

