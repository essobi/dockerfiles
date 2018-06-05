FROM python:2.7.8  
RUN apt-get update ; apt-get install -y fonts-ipafont ; apt-get clean  
RUN pip install blockdiag seqdiag actdiag nwdiag  
VOLUME ["/work"]  
WORKDIR /work  
CMD ["blockdiag","--help"]  

