FROM python:3.5  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
COPY run.py /usr/src/app  
COPY QATrainer.py /usr/src/app  
COPY ./QAGenerators /usr/src/app/QAGenerators  
CMD [ "python","-u", "/usr/src/app/run.py" ]

