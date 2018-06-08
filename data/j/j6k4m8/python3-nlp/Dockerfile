FROM ubuntu:latest  
LABEL maintainer="Jordan Matelsky <open-source@matelsky.com>"  
  
RUN apt-get update  
RUN apt-get install -y git python3-pip  
RUN pip3 install numpy  
RUN pip3 install nltk  
RUN apt-get install -y libevent-dev  
RUN pip3 install spacy  
  
# Download NLTK models:  
RUN python3 -c "import nltk; nltk.download('popular')"  
RUN python3 -m spacy download en  

