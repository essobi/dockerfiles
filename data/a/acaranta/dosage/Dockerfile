FROM ubuntu:16.04  
MAINTAINER arthur@caranta.com  
  
ENV RUNEVERY 7200  
RUN apt-get update && apt-get install -y python3 git python-pip python-lxml
python-cssselect git curl  
#RUN git clone https://github.com/webcomics/dosage.git /app  
RUN git clone https://github.com/acaranta/dosage.git /app  
  
WORKDIR /app  
RUN pip install -r requirements.txt && python setup.py install  
  
RUN mkdir /dosage  
WORKDIR /dosage  
  
CMD dosage $OPTIONS -c @ ; while true; echo "Waiting $RUNEVERY seconds before
next run of dosage"; sleep $RUNEVERY; do dosage $OPTIONS -c @; done  
  

