FROM java:8  
MAINTAINER Ivan Cruz <ivancruz.bht@gmail.com>  
  
ENV CORENLP_ARCHIVE_VERSION=2017-06-09  
ENV CORENLP_SPANISH_MODELS=stanford-spanish-corenlp-  
ENV CORENLP_ARCHIVE=stanford-corenlp-full-${CORENLP_ARCHIVE_VERSION}.zip \  
CORENLP_SHA1SUM=c4fd33b6085d8ac4e8c6746b2c73d95da42d8da4 \  
CORENLP_PATH=/corenlp \  
CORENLP_SHA1_PATH=corenlp.sha1  
  
RUN wget http://nlp.stanford.edu/software/$CORENLP_ARCHIVE  
RUN wget
http://nlp.stanford.edu/software/$CORENLP_SPANISH_MODELS$CORENLP_ARCHIVE_VERSION-
models.jar  
RUN echo "$CORENLP_SHA1SUM $CORENLP_ARCHIVE" > corenlp.sha1 \  
RUN sha1sum -c corenlp.sha1  
RUN unzip $CORENLP_ARCHIVE  
RUN mv $(basename ../$CORENLP_ARCHIVE .zip) $CORENLP_PATH  
RUN mv $CORENLP_SPANISH_MODELS$CORENLP_ARCHIVE_VERSION-models.jar
$CORENLP_PATH  
RUN rm $CORENLP_ARCHIVE  
RUN rm corenlp.sha1  
  
WORKDIR $CORENLP_PATH  
  
EXPOSE 9000  
CMD java -mx4g -cp stanford-corenlp-3.8.0.jar:stanford-spanish-
corenlp-2017-06-09-models.jar edu.stanford.nlp.pipeline.StanfordCoreNLPServer
-annotators tokenize,ssplit,pos,parse,ner 9000

