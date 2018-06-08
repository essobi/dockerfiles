FROM java:8  
MAINTAINER Francesco Komauli <francesco.komauli@gmail.com>  
  
ENV GRADLE_VERSION=2.11  
ENV
GRADLE_URL=https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
ENV
GRADLE_SHA256=8d7437082356c9fd6309a4479c8db307673965546daea445c6c72759cd6b1ed6  
  
VOLUME /project  
ENV GRADLE_HOME /gradle  
ENV GRADLE_USER_HOME /project/.gradle  
  
WORKDIR /tmp  
RUN wget -O gradle.zip $GRADLE_URL \  
&& echo "$GRADLE_SHA256 gradle.zip" | sha256sum -c - \  
&& unzip gradle.zip \  
&& rm gradle.zip \  
&& mv gradle-${GRADLE_VERSION} $GRADLE_HOME \  
&& chmod -R 777 $GRADLE_HOME  
  
ENV PATH $PATH:$GRADLE_HOME/bin  
ENV _JAVA_OPTIONS -Duser.home=$GRADLE_HOME  
  
USER root  
WORKDIR /project  
ENTRYPOINT ["gradle"]  
CMD ["--version"]  

