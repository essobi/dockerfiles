FROM python:3.6  
MAINTAINER Maziar Zamani <maziar@me.com>  
  
COPY ./app/requirements.txt ./requirements.txt  
RUN pip install -U -r requirements.txt  
  
EXPOSE 5000  
COPY ./app /src  
  
WORKDIR /src  
  
CMD ["gunicorn", "app:app.wsgi", "--workers=4", "--bind=0.0.0.0:5000", "--
pid=pid", "--worker-class=meinheld.gmeinheld.MeinheldWorker"]  

