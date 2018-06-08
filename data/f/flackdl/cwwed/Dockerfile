FROM python:3.6.4-stretch  
  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y \  
libgdal-dev \  
postgresql-client \  
&& echo  
  
RUN mkdir /app  
ADD . /app  
WORKDIR /app  
  
RUN pip install -r requirements.txt  
  
EXPOSE 80  
VOLUME /media/bucket/cwwed  
  
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "cwwed.wsgi"]  

