FROM python:2.7  
VOLUME /output  
ADD . /code  
WORKDIR /code  
RUN pip install --no-cache-dir -r requirements.txt  
CMD ["python","twitterstream.py"]

