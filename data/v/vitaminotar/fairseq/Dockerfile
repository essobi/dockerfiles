FROM opennmt/opennmt:latest  
  
RUN sudo apt-get update && \  
sudo apt-get install -y wget git sed  
  
RUN mkdir -p /path/to  
WORKDIR /path/to/  
  
# Install mosesdecoder  
RUN git clone https://github.com/moses-smt/mosesdecoder  
  
RUN git clone https://github.com/facebookresearch/fairseq /root/fairseq  
  
RUN git clone https://github.com/rsennrich/subword-nmt  
  
# Install openNMT  
WORKDIR /root/fairseq  
RUN luarocks make rocks/fairseq-cpu-scm-1.rockspec  
  
RUN curl https://s3.amazonaws.com/fairseq/models/wmt14.en-de.fconv-
float.tar.bz2 | tar xvjf -  
RUN wget -O ~/fairseq/truecase-model.en
http://data.statmt.org/rsennrich/wmt16_systems/en-de/truecase-model.en  
  
RUN wget -O ~/fairseq/translate.sh
https://gist.githubusercontent.com/Khakhulin/f4f8dc457a738b7576302691c9e2af5f/raw/8551b15b87709d8f927623b77d0f82a57c8313fc/translate.sh  
RUN chmod a+x ~/fairseq/translate.sh  
  
RUN mkdir /data  
RUN mkdir /output  
  
CMD ["./translate.sh"]

