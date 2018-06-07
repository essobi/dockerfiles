FROM python:3  
MAINTAINER James Maddox <james@firstjob.com>  
EXPOSE 80  
ENV DISPLACY_SERVICE_PORT 80  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /src  
WORKDIR /src  
ADD requirements.txt .  
RUN pip install -r requirements.txt  
RUN python -m spacy.en.download parser  
ADD . .  
CMD ["python", "app.py"]  

