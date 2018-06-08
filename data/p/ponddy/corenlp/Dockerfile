FROM java:jre-alpine  
  
# Install OS package  
RUN apk add --update --no-cache \  
unzip \  
wget  
  
# Corenlp settings  
RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip
\  
&& unzip stanford-corenlp-full-2017-06-09.zip \  
&& rm stanford-corenlp-full-2017-06-09.zip  
  
# Settings  
ENV PORT 9000  
WORKDIR stanford-corenlp-full-2017-06-09  
  
RUN wget http://nlp.stanford.edu/software/stanford-chinese-
corenlp-2017-06-09-models.jar \  
&& wget http://nlp.stanford.edu/software/stanford-english-
corenlp-2017-06-09-models.jar  
  
# Port  
EXPOSE $PORT  
  
# Run!  
CMD java -Xmx12g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
-serverProperties StanfordCoreNLP-chinese.properties -port 9000 -timeout 15000  

