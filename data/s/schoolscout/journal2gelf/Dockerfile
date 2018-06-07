FROM debian:stable  
  
RUN apt-get update  
RUN apt-get -y install git python-pip  
RUN pip install
git+http://github.com/systemd/journal2gelf.git#egg=journal2gelf  
  
ENTRYPOINT ["journal2gelf"]  

