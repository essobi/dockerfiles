# escape=`  
# Use an official Python runtime as a parent image  
FROM python:2  
LABEL maintainer "andrew.p.moore94@gmail.com"  
RUN apt-get -y update && apt-get install -y cmake gcc default-jdk unzip  
RUN wget https://github.com/apmoore1/TweeboParser/archive/V1.0.1-alpha.zip  
RUN unzip V1.0.1-alpha.zip  
RUN rm V1.0.1-alpha.zip  
WORKDIR TweeboParser-1.0.1-alpha  
RUN echo n | bash install.sh  
RUN pip install --trusted-host pypi.python.org -r requirements.txt  
RUN python -m pytest  
ENTRYPOINT ["python", "tweebo/server.py"]  

