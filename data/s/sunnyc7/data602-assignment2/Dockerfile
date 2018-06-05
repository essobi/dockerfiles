FROM python:3.6  
# Update  
#RUN apt-get update  
RUN pip install --upgrade pip  
COPY requirements.txt /src/requirements.txt  
RUN pip install -r /src/requirements.txt  
  
COPY app.py /src  
COPY schema.sql /src  
COPY trader.db /src  
COPY static /src/static  
COPY templates /src/templates  
COPY trader /src/trader  
WORKDIR /src  
  
EXPOSE 5000  
CMD ["python", "/src/app.py"]  

