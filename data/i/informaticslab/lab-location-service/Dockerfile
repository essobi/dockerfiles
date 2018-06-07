FROM python:3  
COPY main.py main.py  
COPY requirements.txt requirements.txt  
  
ENV FLASK_APP=main.py  
  
RUN pip install -r requirements.txt  
  
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]  

