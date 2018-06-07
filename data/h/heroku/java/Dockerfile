# Inherit from Heroku's stack  
FROM heroku/jvm  
  
# Install Maven  
ENV M2_HOME /app/.mvn  
RUN curl -s --retry 3 -L https://lang-jvm.s3.amazonaws.com/maven-3.3.3.tar.gz
| tar xz -C /app  
RUN chmod +x /app/.maven/bin/mvn  
ENV M2_HOME /app/.maven  
ENV PATH /app/.maven/bin:$PATH  
ENV MAVEN_OPTS "-Xmx1024m -Duser.home=/app/usr
-Dmaven.repo.local=/app/.m2/repository"  
# Run Maven to cache dependencies  
ONBUILD COPY ["pom.xml", "*.properties", "/app/user/"]  
ONBUILD RUN ["mvn", "dependency:resolve"]  
ONBUILD RUN ["mvn", "verify"]  
  
ONBUILD COPY . /app/user/  
ONBUILD RUN ["mvn", "-DskipTests=true", "clean", "package"]  

