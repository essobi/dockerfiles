FROM jfloff/alpine-python:recent  
  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-amd64 /tini  
  
COPY src /stress-test  
  
RUN chmod +x /tini && \  
pip install -r /stress-test/requirements.txt  
  
ENTRYPOINT ["/tini", "-g", "--", "python", "/stress-test/main.py"]  

