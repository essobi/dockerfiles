FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
WORKDIR /code  
  
RUN pip3 install ipython uwsgi  
  
ADD requirements.txt /code  
RUN pip3 install -r requirements.txt  
  
ADD . /code  
  
EXPOSE 8000  
CMD python3 manage.py runserver 0.0.0.0:8000  

