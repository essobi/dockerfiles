FROM python:3.5  
RUN pip install bump  
  
RUN useradd -m bump  
ENV HOME /home/bump  
WORKDIR /home/bump  
COPY bump.sh bump.sh  

