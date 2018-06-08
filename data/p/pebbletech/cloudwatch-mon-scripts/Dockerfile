FROM alpine:3.3  
RUN apk --update add \  
coreutils \  
py-setuptools \  
ca-certificates  
  
RUN mkdir /app  
WORKDIR /app  
  
# Install code:  
COPY setup.py /app  
COPY cloudwatchmon /app/cloudwatchmon  
RUN python setup.py install  
  
# Install wrapper script:  
COPY stats.sh /app  
ENTRYPOINT [ "/app/stats.sh" ]  
  

