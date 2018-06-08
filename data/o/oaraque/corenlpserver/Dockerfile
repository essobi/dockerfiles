FROM java:8-jre-alpine  
MAINTAINER Oscar Araque  
  
RUN mkdir /corenlp  
WORKDIR /corenlp  
  
RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip  
RUN unzip *.zip && rm *.zip  
  
ENV JAVA_OPTS -Xmx2g  
ENV PORT 9000  
CMD java $JAVA_OPTS -cp "./stanford-corenlp-full-2015-12-09/*"
edu.stanford.nlp.pipeline.StanfordCoreNLPServer $PORT  

