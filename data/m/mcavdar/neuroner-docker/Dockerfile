FROM python:3.5-slim  
  
RUN apt-get update && \  
apt-get install python3-pip software-properties-common build-essential unzip
wget -y  
  
COPY requirements.txt requirements.txt  
  
RUN pip install --no-cache -r requirements.txt  
  
RUN python3.5 -m spacy download en  
  
RUN wget https://github.com/mcavdar/NeuroNER/archive/master.zip && \  
unzip master.zip  
  
RUN mkdir NeuroNER-master/data/word_vectors  
  
WORKDIR /NeuroNER-master/data/word_vectors  
  
RUN wget http://neuroner.com/data/word_vectors/glove.6B.100d.zip && \  
unzip glove.6B.100d.zip  
  
EXPOSE 8888  
RUN cd /NeuroNER-master/src  
  
WORKDIR /NeuroNER-master  
  
CMD ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--allow-root", "
--NotebookApp.token='demo'"]  

