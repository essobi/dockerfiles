FROM alpine:3.3  
RUN mkdir /opt; cd /opt; mkdir reTHINK; cd reTHINK; mkdir dev-hyperty; cd dev-
hyperty; mkdir src; mkdir examples;  
  
COPY src/ /opt/reTHINK/dev-hyperty/src/  
COPY examples/ /opt/reTHINK/dev-hyperty/examples/  
  
CMD echo '/opt/reTHINK/dev-hyperty/src' && ls /opt/reTHINK/dev-hyperty/src &&
echo '/opt/reTHINK/dev-hyperty/examples' && ls /opt/reTHINK/dev-
hyperty/examples  

