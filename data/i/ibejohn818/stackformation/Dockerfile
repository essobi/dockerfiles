FROM python:3.5  
RUN apt-get update && apt-get install -y unzip  
RUN apt-get clean  
  
COPY ./requirements.txt /.  
  
RUN pip3 install -r /requirements.txt  
  
RUN pip3 install jh-stackformation  
RUN pip3 install awscli  
  
# Install packer  
RUN curl -L -o /tmp/packer.zip
https://releases.hashicorp.com/packer/1.1.3/packer_1.1.3_linux_amd64.zip?_ga=2.149136882.572918514.1514672601-544189481.1514514079  
  
RUN cd /tmp && unzip packer.zip && mv packer /usr/local/bin/.  
  
CMD []  

