FROM stockport/luigi-taskrunner:latest  
  
MAINTAINER Stockport <info@stockport.gov.uk>  
  
RUN bash -c "source /luigi/.pyenv/bin/activate \  
&& pip install nose pyhamcrest requests"  
  
ADD run.sh /luigi/  
  
ENTRYPOINT ["bash", "/luigi/run.sh"]  

