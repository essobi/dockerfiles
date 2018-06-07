FROM java:8  
ARG GRADLE_VERSION=4.4  
ARG
GRADLE_URL=https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
  
ADD $GRADLE_URL /usr/bin/gradle.zip  
  
WORKDIR /usr/bin  
RUN unzip gradle.zip && \  
rm gradle.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle  
  
ENV GRADLE_HOME /usr/bin/gradle  
ENV GRADLE_USER_HOME /cache/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
VOLUME ["/app", $GRADLE_USER_HOME]  
  
WORKDIR /app  
CMD ["gradle", "--version"]  

