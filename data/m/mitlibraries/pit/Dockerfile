FROM python:3.5  
MAINTAINER Mike Graves <mgraves@mit.edu>  
  
RUN apt-get update && apt-get install -y \  
git  
RUN git clone https://github.com/mitlib-tdm/pit.git  
RUN python3.5 -m pip install -r pit/requirements.txt  
RUN python3.5 -m pip install -e pit/  
  
ENTRYPOINT ["pit"]  
CMD ["--help"]  

