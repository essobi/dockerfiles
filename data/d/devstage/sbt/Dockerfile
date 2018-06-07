FROM java:8  
MAINTAINER Jan Ehrhardt <jan.ehrhardt@gmail.com>  
  
ENV SBT_VERSION 0.13.8  
ADD https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/$SBT_VERSION/sbt-launch.jar /opt/sbt-launch.jar  
  
VOLUME ["/var/lib/sbt"]  
VOLUME ["/var/lib/ivy2"]  
  
ENTRYPOINT ["java", "-Xms512M", "-Xmx1536M", "-Xss1M",
"-XX:+CMSClassUnloadingEnabled", "-Dsbt.global.base=/var/lib/sbt/0.13",
"-Dsbt.ivy.home=/var/lib/ivy2", "-Dsbt.boot.directory=/var/lib/sbt/boot",
"-jar", "/opt/sbt-launch.jar"]  

