######################################################################  
# Builder (stage 0)  
FROM openjdk:8-jdk  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
WORKDIR /omero-ms-thumbnail  
COPY \  
LICENSE.txt \  
README.md \  
build.gradle \  
gradlew \  
/omero-ms-thumbnail/  
COPY gradle/ /omero-ms-thumbnail/gradle/  
COPY src/ /omero-ms-thumbnail/src/  
RUN bash -e gradlew installDist  
  
  
######################################################################  
# Install (stage 1)  
FROM openjdk:8-jre  
  
COPY --from=0 /omero-ms-thumbnail/build/install/omero-ms-thumbnail/
/opt/omero-ms-thumbnail/  
COPY docker/config.json docker/logback.xml /opt/omero-ms-thumbnail/  
  
RUN useradd -m omero  
USER omero  
WORKDIR /home/omero  
ENV JAVA_OPTS "-Dlogback.configurationFile=/opt/omero-ms-
thumbnail/logback.xml"  
CMD ["/opt/omero-ms-thumbnail/bin/omero-ms-thumbnail", "-conf", "/opt/omero-
ms-thumbnail/config.json"]  

