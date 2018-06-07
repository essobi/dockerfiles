FROM python:latest  
  
WORKDIR /usr/src/plotter-http  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
COPY . .  
RUN pip install -e .  
EXPOSE 8000  
CMD [ "python", "./plotter/api.py" ]  
  

