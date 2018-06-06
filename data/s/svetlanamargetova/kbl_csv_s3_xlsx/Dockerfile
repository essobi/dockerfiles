FROM keboola/base  
  
# Initialize  
RUN yum -y install python-pip  
RUN yes | pip install pip xlsxwriter  
RUN yes | pip install tinys3  
  
ADD . /  
WORKDIR /  
  
CMD ["python","code.py"]  

