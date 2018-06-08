FROM django:1.8.5-python3  
MAINTAINER Ovidiu-Florin Bogdan (ovidiu.b13@gmail.com)  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
sqlite3 \  
gcc  
  
EXPOSE 8000  
ENV WORK /usr/src/app/  
  
RUN mkdir -p $WORK  
WORKDIR $WORK  
  
COPY requirements.txt $WORK  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . $WORK  
  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  

