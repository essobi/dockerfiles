FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
WORKDIR /code  
COPY requirements.txt /code  
  
RUN pip install -r requirements.txt --cache-dir $HOME/.cache/pip/  
  
COPY . /code  
RUN pip install -e .  
  
EXPOSE 6543  
CMD pserve development.ini  

