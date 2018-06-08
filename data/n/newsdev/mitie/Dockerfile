FROM python:2.7  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN \  
git clone https://github.com/mit-nlp/MITIE.git && \  
cd MITIE && \  
cd mitielib && \  
make && \  
cd .. && \  
make MITIE-models && \  
rm MITIE-models/english/total_word_feature_extractor.dat && \  
rm MITIE-models-v0.2.tar.bz2  
  
ENV PYTHONPATH $PYTHONPATH:MITIE/mitielib  

