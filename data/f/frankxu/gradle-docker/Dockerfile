FROM java:latest  
  
ENV GRADLE_VERSION 2.9  
RUN curl -fsSL
http://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip -o
/tmp/gradle-$GRADLE_VERSION-bin.zip && unzip /tmp/gradle-$GRADLE_VERSION-
bin.zip -d /usr/share \  
&& rm /tmp/gradle-$GRADLE_VERSION-bin.zip \  
&& mv /usr/share/gradle-$GRADLE_VERSION /usr/share/gradle \  
&& ln -s /usr/share/gradle/bin/gradle /usr/bin/gradle  
  
RUN apt-get install git  
  
ENV GRADLE_HOME /usr/share/gradle  
  
CMD ["gradle"]  

