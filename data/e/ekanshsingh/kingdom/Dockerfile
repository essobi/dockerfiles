FROM python:2-onbuild  
MAINTAINER Ekansh_Singh "ekansh.singh@opscale.io"  
COPY . /app  
WORKDIR /app  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["test01.py"]  

