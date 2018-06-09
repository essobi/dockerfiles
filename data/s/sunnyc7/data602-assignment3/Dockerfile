FROM python:3.6  
RUN pip install numpy  
RUN pip install pandas  
RUN pip install --upgrade pip setuptools  
  
COPY requirements.txt /src/requirements.txt  
RUN pip install --no-cache-dir -r /src/requirements.txt  
  
COPY . /src  
WORKDIR /src  
  
EXPOSE 5000  
CMD ["python", "/src/app.py"]  

