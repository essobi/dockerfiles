FROM python:slim-stretch  
  
WORKDIR /app  
  
ADD . /app  
  
RUN pip install .  
  
EXPOSE 5000  
ENV FLASK_APP server/app.py  
  
CMD ["gunicorn", "server.app:server", "-b :5000", "--no-sendfile"]

