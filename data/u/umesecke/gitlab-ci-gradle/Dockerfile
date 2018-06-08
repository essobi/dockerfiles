FROM java:8-jdk  
MAINTAINER Uwe Mesecke <uwe@mesecke.net>  
  
ENV GRADLE_VERSION=3.0  
ENV
GRADLE_URL=https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
ENV
GRADLE_SHA256=39c906941a474444afbddc38144ed44166825acb0a57b0551dddb04bbf157f80  
  
ENV GRADLE_HOME /opt/gradle  
  
WORKDIR /opt/  
RUN wget -O gradle.zip $GRADLE_URL \  
&& echo "$GRADLE_SHA256 gradle.zip" | sha256sum -c - \  
&& unzip gradle.zip \  
&& rm gradle.zip \  
&& mv gradle-${GRADLE_VERSION} $GRADLE_HOME \  
&& chmod -R 777 $GRADLE_HOME  
  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
ENV PATH $PATH:$GRADLE_HOME/bin  
ENV GRADLE_USER_HOME /cache/.gradle  
  
COPY cmd.sh /  
  
USER root  
VOLUME /cache  
VOLUME /builds  
WORKDIR /builds  
ENTRYPOINT ["/cmd.sh"]  

