FROM ubuntu:16.04  
RUN echo >> /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y software-properties-common python3
python3-pip && rm -rf /var/lib/apt/lists/*  
  
RUN add-apt-repository ppa:ethereum/ethereum && apt-get update && apt-get
install -y solc && rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install flask twilio web3 py-solc  
  
EXPOSE 5000  
COPY *.py /  
  
ENTRYPOINT ["python3", "/flaskExample.py"]

