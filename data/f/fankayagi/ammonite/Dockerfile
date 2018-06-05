FROM ubuntu:16.04  
LABEL maintainer "Kazuo Yagi <ka_yagi@fancs.com>"  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="GNU GENERAL PUBLIC LICENSE Version 3" \  
org.label-schema.name="fan-ka-yagi/ammonite" \  
org.label-schema.url="https://github.com/fan-ka-yagi/ammonite" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/fan-ka-yagi/ammonite"  
  
# Install JDK, misc packages.  
RUN apt-get update && apt-get install -y \  
default-jdk \  
apt-transport-https \  
curl \  
vim  
  
# Install sbt. See http://www.scala-sbt.org/1.0/docs/Installing-sbt-on-
Linux.html  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823  
RUN apt-get update && apt-get install -y sbt  
  
# Install ammonite. See http://ammonite.io/#Ammonite-REPL  
RUN curl -L -o /usr/bin/amm https://git.io/vdNv2 && chmod +x /usr/bin/amm &&
mkdir /root/.ammonite  
  
# Add libraries.  
WORKDIR /root  
RUN echo '// This is ammonite rc file.\n\  
import $ivy.`com.lihaoyi::ammonite-ops:1.0.3`, ammonite.ops._\n\  
import $ivy.`org.typelevel::cats-core:1.0.1`\n\  
import $ivy.`com.chuusai::shapeless:2.3.3`\n\  
import $ivy.`co.fs2::fs2-core:0.10.0-RC1`\n\  
import $ivy.`co.fs2::fs2-io:0.10.0-RC1`\n\  
import $ivy.`org.tpolecat::doobie-core:0.5.0-RC1`\n\  
import $ivy.`org.tpolecat::doobie-h2:0.5.0-RC1`\n\  
import $ivy.`org.tpolecat::doobie-hikari:0.5.0-RC1`\n\  
import $ivy.`org.tpolecat::doobie-postgres:0.5.0-RC1`\n\  
import $ivy.`org.tpolecat::doobie-specs2:0.5.0-RC1`\n\  
import $ivy.`org.tpolecat::doobie-scalatest:0.5.0-RC1`\n\  
import $ivy.`io.circe::circe-core:0.9.1`\n\  
import $ivy.`io.circe::circe-generic:0.9.1`\n\  
import $ivy.`io.circe::circe-parser:0.9.1`\n\  
' > /root/.ammonite/predef.sc  
  
# Cache libraries.  
RUN export TERM=vt100 && script -qfc 'echo exit | amm -s' && rm typescript  

