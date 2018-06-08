FROM java:jre-alpine  
  
MAINTAINER Shayne Miel <miel.shayne@gmail.com>  
  
RUN apk add --update --no-cache \  
unzip \  
wget  
  
ARG CORENLP_RELEASE=stanford-corenlp-full-2016-10-31  
RUN wget http://nlp.stanford.edu/software/$CORENLP_RELEASE.zip  
RUN unzip $CORENLP_RELEASE.zip && \  
rm $CORENLP_RELEASE.zip  
  
WORKDIR $CORENLP_RELEASE  
  
RUN wget https://nlp.stanford.edu/software/stanford-
srparser-2014-10-23-models.jar  
  
RUN export CLASSPATH="`find . -name '*.jar'`"  
  
ENV PORT 9000  
EXPOSE $PORT  
  
COPY sr_beam.props sr_beam.props  
  
CMD java -cp "*" -mx8g edu.stanford.nlp.pipeline.StanfordCoreNLPServer
-serverProperties sr_beam.props  

