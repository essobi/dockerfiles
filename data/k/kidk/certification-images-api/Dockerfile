FROM python:2-onbuild  
MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>  
  
COPY main.py /src/main.py  
COPY generic.py /src/generic.py  
  
EXPOSE 8000  
CMD ["python", "/src/main.py", "-p 8000"]  

