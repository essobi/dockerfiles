FROM ubuntu:trusty  
  
RUN apt-get update \  
&& apt-get install -y python python-dev python-pip python-virtualenv \  
&& pip install -U pip \  
&& pip install pdfminer==20140328 \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /pdf  
WORKDIR /pdf  
  
ENTRYPOINT ["pdf2txt.py"]  
# CMD ["-o"]  

