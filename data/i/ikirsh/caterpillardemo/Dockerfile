FROM ubuntu:16.04  
LABEL maintainer "None"  
  
RUN apt-get update && apt-get install -y --no-install-recommends python  
RUN apt-get update && apt-get install -y --no-install-recommends python-pip  
RUN pip install --upgrade pip  
RUN pip install setuptools  
RUN pip install flask  
RUN pip install flask-login  
RUN pip install flask-openid  
RUN pip install flask-mail  
RUN pip install flask-sqlalchemy  
RUN pip install sqlalchemy-migrate  
RUN pip install flask-whooshalchemy  
RUN pip install flask-wtf  
RUN pip install flask-babel  
RUN pip install flask-mysql  
RUN pip install guess_language  
RUN pip install flipflop  
RUN pip install coverage  
RUN pip install pymysql  
  
EXPOSE 5000  
RUN mkdir /web  
RUN mkdir /web/app  
ADD ./run.py /web/  
ADD ./app /web/app/  
  
WORKDIR /web  
ENTRYPOINT ["python"]  
CMD ["run.py"]  

