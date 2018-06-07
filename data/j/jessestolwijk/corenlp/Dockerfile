FROM java:8  
MAINTAINER Jesse Stolwijk <stolwijkjesse@gmail.com>  
  
ENV FILENAME stanford-corenlp-full-2018-01-31  
ENV FILE ${FILENAME}.zip  
  
RUN apt-get update && apt-get install -y \  
unzip \  
wget  
  
RUN wget http://nlp.stanford.edu/software/${FILE}  
  
RUN unzip ${FILE} && \  
rm ${FILE}  
  
WORKDIR ${FILENAME}  
RUN export CLASSPATH="`find . -name '*.jar'`"  
  
ENV PORT 9000  
EXPOSE $PORT  
  
CMD java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer --port
$PORT \--timeout 10000  

