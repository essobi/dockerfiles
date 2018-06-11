FROM python:3.6  
# This creates a docker image with all the requirements for building  
WORKDIR /app  
RUN pip install --upgrade pip  
  
COPY ./requirements.txt /app/  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
CMD [ "bash" ]

