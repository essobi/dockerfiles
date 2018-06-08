FROM mikeneck/jdk8  
  
MAINTAINER Shinya Mochida(mikeneck - twitter:@mike_neck)  
  
RUN \  
groupadd -r build && \  
useradd -m -g build gradle  
  
WORKDIR /home/gradle  
  
RUN \  
curl -L https://services.gradle.org/distributions/gradle-2.9-all.zip -o
gradle.zip  
  
RUN \  
unzip -q gradle.zip -d tmp && \  
mkdir gradle && \  
mv tmp/gradle-2.9/bin gradle/ && \  
mv tmp/gradle-2.9/lib gradle/ && \  
mv tmp/gradle-2.9/init.d gradle/ && \  
rm -rf tmp && \  
rm gradle.zip && \  
mkdir /home/gradle/.gradle && \  
mkdir /home/gradle/project  
  
VOLUME /home/gradle/.gradle  
VOLUME /home/gradle/project  
  
RUN \  
chown -R gradle /home/gradle/gradle && \  
chown gradle /home/gradle/.gradle && \  
chown gradle /home/gradle/project  
  
USER gradle  
  
ENV GRADLE_HOME /home/gradle/gradle  
ENV PATH=$PATH:$GRADLE_HOME/bin  
  
CMD ["/bin/bash"]  

