FROM pyannote/core  
MAINTAINER Hervé Bredin <bredin@limsi.fr>  
  
ADD . /src  
RUN pip install /src  
  
CMD ["python", "-m", "pyannote.server.run"]  
EXPOSE 5000  

