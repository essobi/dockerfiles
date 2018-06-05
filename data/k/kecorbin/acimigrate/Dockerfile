FROM python:2-onbuild  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
EXPOSE 8000  
CMD [ "python", "./main.py" ]  

