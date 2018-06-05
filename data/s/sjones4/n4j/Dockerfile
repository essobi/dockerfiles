FROM gradle:4.1-jdk8  
  
ADD [ "n4j.sh", "build.gradle", "settings.gradle", "endpoints.xml",
"3wolfmoon-download.jpg", "test.dat", "/home/gradle/n4j/" ]  
ADD [ "src", "/home/gradle/n4j/src/" ]  
  
USER root  
RUN mkdir --parents /n4j/cache/images \  
&& mkdir --parents /n4j/results \  
&& mkdir --parents /n4j/cache/.gradle \  
&& chown --recursive gradle:gradle /n4j/cache \  
&& chown --recursive gradle:gradle /n4j/results \  
&& chown --recursive gradle:gradle /home/gradle/n4j  
  
USER gradle  
WORKDIR /home/gradle/n4j  
ENV GRADLE_USER_HOME="/n4j/cache/.gradle" \  
N4J_RESULTS="/n4j/results" \  
N4J_OPTS="-Dcache=/n4j/cache"  
VOLUME /n4j/cache  
VOLUME /n4j/results  
  
CMD ./n4j.sh  
  

