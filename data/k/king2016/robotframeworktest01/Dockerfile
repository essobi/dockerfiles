FROM ubuntu:16.04  
RUN apt-get update && apt-get install python-pip -y  
RUN pip install robotframework  
RUN pip install robotframework-selenium2library  
RUN pip install xvfbwrapper  
RUN apt-get update  
RUN apt-get install xvfb -y  
RUN pip install robotframework-xvfb  
RUN pip install --upgrade robotframework-httplibrary  
VOLUME /reports  
CMD ["pybot","--help"]  

