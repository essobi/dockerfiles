FROM golang:1.7.4-wheezy  
  
RUN mkdir /src && mkdir /src/fresh8-gb-ci/ \  
apt-get update && \  
apt-get install git python && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install pyyaml  
COPY ./*.py /src/fresh8-gb-ci/  
VOLUME ["/src"]  
  
ENV GOPATH=/src:/src/vendor  
  
#ENTRYPOINT ["python", "/src/fresh8-gb-ci/ci.py", "/src/"]  
CMD cd /src/ && python fresh8-gb-ci/ci.py  

