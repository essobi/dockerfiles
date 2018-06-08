FROM advancedclimatesystems/python:2.7.10  
MAINTAINER Auke Willem Oosterhoff <auke@orangetux.nl>  
  
RUN pip install sphinx  
  
WORKDIR /src  
  
CMD sphinx-build -b html docs/source/ docs/build/  

