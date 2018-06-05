FROM qcifengineering/gradle:3.5  
ENV PROJECT_HOME=/home/groovy/acceptance  
WORKDIR $PROJECT_HOME  
COPY buildSrc/src ${PROJECT_HOME}/buildSrc/src  
COPY buildSrc/build.gradle ${PROJECT_HOME}/buildSrc/  
COPY src ${PROJECT_HOME}/src  
COPY build.gradle ${PROJECT_HOME}/  
COPY gradle/*.gradle ${PROJECT_HOME}/gradle/  
USER root  
RUN chown -R groovy:groovy /home/groovy  
USER groovy  
#ensure max dependencies present in image, so tests can move quickly  
RUN gradle clean && \  
gradle unpackSauceConnect && \  
gradle compileTestJava && \  
gradle compileTestGroovy && \  
## sanity check against any saucelabs issues - have phantomjs available  
gradle downloadPhantomjs && \  
gradle unzipPhantomjs  
VOLUME ${GRADLE_HOME}/.gradle  
CMD ["gradle"]

