FROM python:3.4  
EXPOSE 8000  
RUN pip install mkdocs  
  
RUN mkdir /documents  
RUN mkdir /site  
WORKDIR /documents  
  
CMD mkdocs serve  

