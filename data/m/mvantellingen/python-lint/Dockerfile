FROM python:3.6.1  
  
RUN useradd --system --user-group linter  
  
COPY requirements.txt /  
RUN pip install -r /requirements.txt  
  
USER linter  
WORKDIR /code/  

