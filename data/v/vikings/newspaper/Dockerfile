FROM python:3  
COPY ./requirements.txt /Newspaper/requirements.txt  
WORKDIR /Newspaper  
RUN pip3 install -r requirements.txt  
ADD . /Newspaper  
ENV FLASK_APP=main.py  
RUN python3 /Newspaper/install.py  
EXPOSE 5000  
ENTRYPOINT ["python3"]  
  
CMD ["-m","flask","run","--host=0.0.0.0"]

