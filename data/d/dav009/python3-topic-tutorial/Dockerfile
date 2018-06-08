FROM dataquestio/python3-starter  
  
RUN /opt/ds/bin/pip install nltk && \  
mkdir ~/nltk_data && \  
mkdir ~/nltk_data/chunkers && \  
mkdir ~/nltk_data/corpora && \  
mkdir ~/nltk_data/taggers && \  
mkdir ~/nltk_data/tokenizers && \  
/opt/ds/bin/python3 -c "import nltk; nltk.download(['punkt',
'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words', 'stopwords'])"  
  
RUN /opt/ds/bin/pip install gensim==0.13.1 pyLDAvis matplotlib==1.5.2

