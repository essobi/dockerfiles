FROM java:8  
MAINTAINER Isaac Wong (iwong@uncharted.software)  
  
RUN apt-get update  
  
# nodejs 4 executable  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install --yes nodejs  
  
# install utility packages  
RUN apt-get install bzip2  
  
# install Phantomjs  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /bin/ \  
&& rm -rf phantomjs-2.1.1-linux-x86_64 phantomjs-2.1.1-linux-x86_64.tar.bz2  
  
# install Stanford NER  
RUN curl http://nlp.stanford.edu/software/stanford-ner-2015-04-20.zip --output
/ner.zip  
RUN unzip -q /ner.zip -d /temp-ner \  
&& cp -ar /temp-ner/stanford-ner-2015-04-20/ /stanford-ner \  
&& rm -rf /temp-ner ner.zip  
  

