FROM python:3  
COPY app.py /  
COPY CollationParser /CollationParser  
COPY static /static  
COPY templates /templates  
  
RUN pip install flask  
RUN pip install SPARQLWrapper  
  
CMD [ "python", "./app.py" ]  

