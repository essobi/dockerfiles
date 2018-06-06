FROM python:alpine  
  
ADD patchalerts ./patchalerts/  
ADD requirements.txt ./  
  
RUN pip install -r ./requirements.txt  
RUN python -V  
  
ENTRYPOINT [ "python", "-u", "./patchalerts/scanner.py"]

