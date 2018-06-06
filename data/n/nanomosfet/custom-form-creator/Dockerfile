FROM python:slim-stretch  
  
WORKDIR /app  
  
ADD . /app  
  
RUN pip install flask==0.12  
  
EXPOSE 5000  
EXPOSE 80  
ENV FLASK_APP server/app.py  
  
CMD ["flask", "run", "--host=0.0.0.0"]

