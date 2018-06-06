FROM idio/spark-singlenode:latest  
MAINTAINER David Przybilla <david.przybilla@idioplatform.com>  
  
ENV LANGUAGE en  
ENV JSONWIKIPEDIA_VERSION 1.1.0  
ENV JSONWIKIPEDIA_JAR /json-wikipedia-master/target/json-
wikipedia-${JSONWIKIPEDIA_VERSION}-jar-with-dependencies.jar  
  
## json-wikipedia  
ADD https://github.com/idio/json-wikipedia/archive/master.zip ./jsonpedia-
master.zip  
RUN unzip jsonpedia-master.zip  
WORKDIR json-wikipedia-master  
RUN mvn assembly:assembly  
RUN ln -s $JSONWIKIPEDIA_JAR /usr/bin/jsonwikipedia.jar  
  
## Generates Jsonpedia  
ENTRYPOINT [ "/var/lib/spark/bin/spark-submit", "--driver-memory", "20G", "--
class", "it.cnr.isti.hpc.wikipedia.cli.MediawikiToJsonCLI",
"/usr/bin/jsonwikipedia.jar"]  

