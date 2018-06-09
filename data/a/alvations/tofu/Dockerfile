  
FROM ubuntu:latest  
  
MAINTAINER Tofu <to@fu.com>  
LABEL description="Tofu Tokenization Kit."  
  
# Update Ubuntu.  
RUN apt-get update  
RUN apt-get install -y apt-utils debconf-utils  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update && apt-get -y upgrade  
  
# Install some necessary tools.  
RUN apt-get install -y sudo nano perl python-dev python3-dev python-pip
python3-pip  
RUN apt-get install -y curl wget tar dtrx unzip git  
  
# Install Java.  
RUN apt-get install -y default-jre default-jdk  
  
# Download Stanford Stuff.  
RUN mkdir /tokenizers/  
WORKDIR /tokenizers/  
RUN wget https://nlp.stanford.edu/software/stanford-segmenter-2016-10-31.zip  
RUN unzip stanford-segmenter-2016-10-31.zip  
RUN mv /tokenizers/stanford-segmenter-2016-10-31/data /tokenizers/  
RUN mv /tokenizers/data/ /tokenizers/stanfordsegmenterdata/  
RUN mv /tokenizers/stanford-segmenter-2016-10-31/segment.sh /tokenizers/  
RUN perl -pi -e 's|\$BASEDIR\/data|\$BASEDIR\/stanfordsegmenterdata|g'
segment.sh  
RUN mv /tokenizers/stanford-segmenter-2016-10-31/stanford-segmenter-3.7.0.jar
/tokenizers/  
RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip  
RUN unzip stanford-corenlp-full-2016-10-31.zip  
RUN mv /tokenizers/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar
/tokenizers/  
COPY tokenize-zh.sh /tokenizers/tokenize-zh.sh  
COPY tokenize-en.sh /tokenizers/tokenize-en.sh  
COPY percsplit.sh /tokenizers/percsplit.sh  
RUN chmod +x /tokenizers/percsplit.sh  
RUN rm stanford-corenlp-full-2016-10-31.zip stanford-segmenter-2016-10-31.zip  
RUN rm -rf /tokenizers/stanford-segmenter-2016-10-31/  
RUN rm -rf /tokenizers/stanford-corenlp-full-2016-10-31/  
  
# Download Moses tokenizer.  
RUN wget https://github.com/nltk/nltk_data/raw/gh-
pages/packages/corpora/nonbreaking_prefixes.zip  
RUN mkdir /share/  
RUN unzip nonbreaking_prefixes.zip -d /share/  
COPY tokenizer.perl /tokenizers/tokenizer.perl  
COPY clean-corpus-n.perl /tokenizers/clean-corpus-n.perl  
RUN chmod +x /tokenizers/tokenizer.perl  
RUN chmod +x /tokenizers/clean-corpus-n.perl  
  
# Download Paddle preprocessing.  
RUN pip install -U docopt  
COPY preprocess.py /tokenizers/preprocess.py  
COPY preprocess_util.py /tokenizers/preprocess_util.py  
  
# Download files to convert Paddle seq2seq inputs to Moses inputs  
COPY paddle2moses.sh /tokenizers/paddle2moses.sh  
WORKDIR /  

