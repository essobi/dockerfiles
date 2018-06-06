FROM tiangolo/uwsgi-nginx-flask:python3.6  
  
RUN apt-get update && apt-get -y install build-essential  
  
RUN pip3 install connexion==1.2  
RUN pip3 install spacy==2.0.5  
RUN pip3 install nltk==3.2.5  
RUN pip3 install scipy==0.19.1  
RUN pip3 install scikit-learn==0.19.1  
RUN pip3 install numpy==1.14.0  
  
RUN python3 -m nltk.downloader all  
RUN python3 -m spacy download en  

