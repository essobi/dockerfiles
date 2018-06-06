FROM python:2  
ADD . /pdfmagic  
WORKDIR /pdfmagic  
RUN pip install --upgrade -r ./requirements.txt  
EXPOSE 8080 8080  
CMD ["python", "pdfmagic.py"]  

