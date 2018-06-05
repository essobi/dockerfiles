FROM python:3.6  
MAINTAINER Joseph Walton <joseph.walton@ons.gov.uk>  
  
WORKDIR /app  
COPY . /app  
EXPOSE 8001  
RUN pip3 install pipenv==8.3.1 && pipenv install --deploy --system  
  
ENTRYPOINT ["python3"]  
CMD ["run.py"]  

