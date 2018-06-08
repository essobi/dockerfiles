FROM python:3  
WORKDIR /home  
  
# so we can easily swap models  
ENV SPACY_NER_MODEL=en_core_web_sm  
  
RUN pip install "spacy==1.8.2" \  
"falcon" \  
"pytest" \  
"gunicorn" \  
&& python -m spacy download $SPACY_NER_MODEL  
  
RUN git clone https://github.com/papadp/spacy-services  
  
WORKDIR /home/spacy-services  
  
EXPOSE 8000  
CMD python ./app.py  

