FROM python:3.6.1  
ENV LANG en  
  
RUN pip install --upgrade pip setuptools  
RUN pip install "spacy==1.2.0"  
RUN python -m spacy.${LANG}.download \  
&& rm -fr /usr/local/lib/python3.6/site-packages/spacy/data/__cache__  

