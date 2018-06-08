FROM java:8  
MAINTAINER Artjom31415 <artjom31415@googlemail.com>  
  
# SBT installation copied from william-yeh/docker-sbt  
ENV SBT_VERSION 0.13.8  
ENV SBT_JAR https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/$SBT_VERSION/sbt-launch.jar  
  
  
ADD $SBT_JAR /usr/local/bin/sbt-launch.jar  
COPY sbt.sh /usr/local/bin/sbt  
  
RUN echo "==> fetch all sbt jars from Maven repo..." && \  
echo "==> [CAUTION] this may take several minutes!!!" && \  
sbt  
  
# Install R  
RUN apt-get clean && apt-get update && apt-get install -y r-base r-base-dev  
  
# Install necessary packages  
RUN apt-get clean && apt-get update && apt-get install -y libgeos-dev libgdal-
dev libproj-dev  
RUN R -e 'install.packages(c("rjson", "rgdal", "rgeos", "ggmap"),
repos="http://cran.us.r-project.org")'  
  
ENV R_HOME=/usr/lib/R  
  
WORKDIR /app

