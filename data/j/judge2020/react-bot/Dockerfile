FROM python:3  
WORKDIR /approot  
  
# Pip is set up to use cache  
ADD ./requirements.txt /approot/requirements.txt  
RUN pip install -r requirements.txt  
  
COPY . /approot  
  
CMD ["python", "./ReactBot.py"]

