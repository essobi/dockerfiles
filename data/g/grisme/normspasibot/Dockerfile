FROM python:3  
ADD bot.py /  
ADD requirements.txt /  
  
RUN pip install -r /requirements.txt  
  
CMD ["python", "/bot.py", "SECRET_TOKEN"]

