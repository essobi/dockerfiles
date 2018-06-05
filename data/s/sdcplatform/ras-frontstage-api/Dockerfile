FROM python:3.6  
WORKDIR /app  
COPY . /app  
EXPOSE 8083  
RUN pip3 install pipenv==8.3.2 && pipenv install --system --deploy  
  
ENTRYPOINT ["python3"]  
CMD ["run.py"]  

