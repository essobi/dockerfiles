FROM coala/base  
MAINTAINER Lasse Schuirmann lasse.schuirmann@gmail.com  
  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt  
  
RUN mkdir -p /usr/src/subject  
  
WORKDIR /usr/src/app  
CMD [ "python3", "run_coala.py" ]  

