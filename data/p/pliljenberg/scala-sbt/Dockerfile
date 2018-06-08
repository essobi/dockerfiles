FROM frolvlad/alpine-oraclejdk8:8.131.11-slim  
  
ENV SBT_HOME /usr/bin/sbt  
  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
RUN apk add --no-cache bash ncurses git  
  
RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates
openssl && mkdir -p ${SBT_HOME} && wget -qO-
https://downloads.lightbend.com/scala/2.12.4/scala-2.12.4.tgz | tar xz -C
/root/ && echo 'export PATH=~/scala-2.12.4/bin:$PATH' >> /root/.bashrc && wget
-qO- - --no-check-certificate
https://github.com/sbt/sbt/releases/download/v1.0.4/sbt-1.0.4.tgz | tar xz -C
$SBT_HOME \--strip-components=1 && mkdir -p /root/.sbt/1.0/plugins && echo
'addSbtPlugin("io.get-coursier" % "sbt-coursier" % "1.0.1-M1")' >>
/root/.sbt/1.0/plugins/plugins.sbt && echo 'classpathTypes += "maven-plugin"'
>> /root/.sbt/1.0/sbt-coursier.sbt && mkdir project && echo 'scalaVersion :=
"2.12.4"' > build.sbt && echo 'sbt.version=1.0.4' > project/build.properties
&& sbt update && rm -r project && rm build.sbt && apk del build-dependencies  
  
WORKDIR /root  

