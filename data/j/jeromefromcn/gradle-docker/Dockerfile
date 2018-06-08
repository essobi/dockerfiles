FROM java:8-jdk  
MAINTAINER Jerome Jiang "jeromefromcn@gmail.com"  
# Gradle  
WORKDIR /usr/bin  
RUN wget https://services.gradle.org/distributions/gradle-2.6-bin.zip && \  
unzip gradle-2.6-bin.zip && \  
ln -s gradle-2.6 gradle && \  
rm gradle-2.6-bin.zip  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
ADD assets/ /app/  
RUN chmod 755 /app/setup/install  
RUN /app/setup/install  

