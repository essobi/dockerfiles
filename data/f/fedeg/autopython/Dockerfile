FROM python:latest  
MAINTAINER Federico Gonzalez (https://github.com/fedeg/)  
  
RUN mkdir -p . /src  
WORKDIR /src  
RUN pip install colorama pygments  
RUN pip install autopython  
  
ENTRYPOINT ["autopython"]  

