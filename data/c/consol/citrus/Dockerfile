FROM maven:3.5.0-jdk-8  
MAINTAINER citrusframework.org <citrus-dev-l@consol.de>  
  
ENV BUILD_DATE=2018-05-14  
RUN mkdir citrus-project  
RUN mkdir -p citrus-project/src/test/java/com/consol/citrus/  
  
COPY assets/pom.xml citrus-project/  
COPY assets/SampleIT.java citrus-project/src/test/java/com/consol/citrus/  
  
# Download all dependencies with compile and skip tests, we use a simple
install and clean the 'target' folder afterwards. This way almost all
dependencies are bundled in the local m2 repo.  
RUN mvn -f citrus-project/pom.xml install clean  
  
ENV APP_DIR /maven  
  
WORKDIR ${APP_DIR}  
  
CMD mvn install

