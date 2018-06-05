FROM python:3  
MAINTAINER James Maddox <james@firstjob.com>  
EXPOSE 80  
ENV SERVICE_PORT 80  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /src  
WORKDIR /src  
ADD . .  
RUN pip install -r requirements.txt  
CMD ["python", "brat_displacy_adapter.py"]  

