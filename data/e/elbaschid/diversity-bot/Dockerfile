FROM python:3.5.2-slim  
MAINTAINER Sebastian Vetter <seb@roadsi.de>  
  
RUN mkdir -p /app  
WORKDIR /app  
  
ADD ./requirements.txt /app/requirements.txt  
RUN pip install -r requirements.txt  
  
ADD . /app  
CMD ["python", "diversity/bot.py"]  

