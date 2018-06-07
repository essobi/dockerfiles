FROM ubuntu:16.04  
ENV LANG C.UTF-8  
RUN apt update  
RUN apt install -y python3 python3-pip git  
  
RUN git clone https://github.com/hobozhang/pyusic-api.git  
RUN pip3 install --upgrade pip  
RUN pip3 install -r pyusic-api/requirements.txt  
  
EXPOSE 5000  
WORKDIR /pyusic-api  
CMD python3 run_server.py  

