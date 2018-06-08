FROM python:3.6  
WORKDIR /usr/src/app  
COPY requirements.txt ./  
RUN pip install --upgrade pip  
RUN pip install --no-cache-dir -r requirements.txt  
RUN git clone https://github.com/john-grando/data602-finalproject.git
/usr/src/app/python-final-project  
EXPOSE 5000  
CMD [ "python", "/usr/src/app/python-final-project/app.py" ]  

