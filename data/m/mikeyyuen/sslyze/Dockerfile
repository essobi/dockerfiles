FROM python:3.6  
RUN apt-get update && apt-get install gcc && apt-get clean -y  
RUN pip install --upgrade pip && pip install sslyze  
  
ENTRYPOINT [ "/usr/local/bin/sslyze" ]  
  
CMD [ "-h" ]  
  

