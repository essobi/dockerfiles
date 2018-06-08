FROM python:3  
COPY ./requirements.txt /Night/requirements.txt  
WORKDIR /Night  
RUN pip3 install -r requirements.txt  
ADD . /Night  
ENV FLASK_APP=main.py  
  
EXPOSE 5000  
ENTRYPOINT ["python3"]  
  
CMD ["-m","flask","run","--host=0.0.0.0"]  

