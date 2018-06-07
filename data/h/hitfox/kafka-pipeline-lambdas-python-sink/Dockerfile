FROM julianbei/python2.7-nlp  
  
RUN mkdir /app  
COPY ./requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
COPY ./ ./  
  
CMD [ "python", "-u", "server.py" ]  

