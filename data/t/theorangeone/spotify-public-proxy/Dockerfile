FROM python:3.6-alpine  
  
RUN apk add --no-cache gcc libc-dev make  
  
COPY ./src /app/src  
COPY ./requirements.txt /app  
  
WORKDIR /app  
  
RUN pip install -r requirements.txt  
  
RUN apk del --no-cache gcc libc-dev make  
  
CMD python3 /app/src/app.py  
  
EXPOSE 5000  

