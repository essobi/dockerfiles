FROM fujitsudas/pipeline-springboot-cloud-gradle  
  
MAINTAINER Emmanuel Pirsch <emmanuel@pirsch.org>  
  
ADD sample-owasp-sonar /sample-owasp-sonar  
  
RUN cd sample-owasp-sonar && ./gradlew --no-daemon clean build
dependencyCheckAnalyze || echo "Failed, really!" && cd ..  

