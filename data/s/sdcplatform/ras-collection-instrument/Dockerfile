FROM python:3.6  
WORKDIR /app  
COPY . /app  
EXPOSE 8002  
RUN pip3 install pipenv==8.3.1 && pipenv install --deploy --system  
  
ENTRYPOINT ["python3"]  
CMD ["run.py"]

