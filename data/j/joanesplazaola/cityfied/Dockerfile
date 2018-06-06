FROM python:3.6  
RUN mkdir /code  
WORKDIR /code  
ADD . /code/  
RUN apt-get update && apt-get install -y gcc unixodbc-dev  
RUN pip install -r cityfied_hems/requirements.txt  
  
EXPOSE 8000  
CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]

