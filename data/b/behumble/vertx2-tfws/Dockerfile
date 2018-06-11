FROM openjdk:8-jre  
MAINTAINER Alan Goo <behumble@hanjava.net>  
  
ENV VERTX_HOME /vert.x-2.1.6  
ENV PATH $PATH:$VERTX_HOME/bin  
ENV VERTX_MODS $VERTX_HOME/mods  
  
RUN curl -L
https://bintray.com/vertx/downloads/download_file?file_path=vert.x-2.1.6.tar.gz
| tar xz  
RUN rm -f $VERTX_HOME/lib/jackson-*  
RUN wget -P $VERTX_HOME/lib
http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-
annotations/2.6.6/jackson-annotations-2.6.6.jar  
RUN wget -P $VERTX_HOME/lib
http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-
core/2.6.6/jackson-core-2.6.6.jar  
RUN wget -P $VERTX_HOME/lib
http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-
databind/2.6.6/jackson-databind-2.6.6.jar  
  
VOLUME ["$VERTX_MODS", "/modzip"]  
  
CMD ["sh", "-c", "$VERTX_HOME/bin/vertx"]  

