FROM java:8-jdk  
MAINTAINER Dmytro Serdiuk <dmytro.serdiuk@gmai.com>  
  
LABEL Description="This image is used to show the Allure reposting"  
LABEL Vendor="extsoft"  
LABEL Version="1.0.0"  
  
ENV MAIN_JAR 'allure-docker-example-1.2.0.jar'  
ENV ASPECT_JAR 'deps/aspectjweaver-1.8.0.jar'  
ENV GRADLE_VERSION 2.13  
ENV MAIN_DIR /allure-docker-example  
ENV BUILD_DIR ${MAIN_DIR}/build  
  
# Update packages and install dependencies  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
RUN apt-get install -fy unzip git  
  
# Install Gradle  
RUN wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip gradle-${GRADLE_VERSION}-bin.zip && \  
mv gradle-${GRADLE_VERSION} /opt/ && \  
rm gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_HOME /opt/gradle-${GRADLE_VERSION}  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Inslate Allure CLI  
RUN wget https://github.com/allure-framework/allure-
core/releases/download/allure-core-1.4.24.RC2/allure-commandline.zip && \  
unzip allure-commandline.zip && bin/allure && rm allure-commandline.zip  
  
# Prepare jars  
WORKDIR ${BUILD_DIR}  
COPY src ${BUILD_DIR}/src/  
COPY build.gradle ${BUILD_DIR}  
COPY gradle.properties ${BUILD_DIR}  
COPY settings.gradle ${BUILD_DIR}  
RUN gradle  
  
# Set up and clean up  
WORKDIR ${MAIN_DIR}  
RUN cp -r ${BUILD_DIR}/build/libs/* .  
RUN rm -r ${BUILD_DIR}  
  
#Run tests, generate and open report  
CMD java -javaagent:${ASPECT_JAR} -jar ${MAIN_JAR} && \  
allure generate -o allure-report allure-result && \  
allure report open -p 80

