FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y \  
git \  
python-pip  
  
RUN git clone https://github.com/oicr-softeng/aws-reporting.git  
RUN pip install boto  
WORKDIR aws-reporting/  
RUN mkdir reports  

