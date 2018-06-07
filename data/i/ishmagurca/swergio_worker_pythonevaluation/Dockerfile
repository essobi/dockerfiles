FROM python:3.5  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
COPY run.py /usr/src/app  
COPY pythonEvaluation.py /usr/src/app  
COPY ./Executables /usr/src/app/Executables  
CMD [ "python","-u", "/usr/src/app/run.py" ]

