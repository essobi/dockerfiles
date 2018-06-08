FROM alpine  
  
VOLUME /openstackinfo  
  
RUN apk add --update ca-certificates python3 python3-dev linux-headers musl-
dev gcc bash && \  
pip3 install python-glanceclient && \  
apk del linux-headers python3-dev musl-dev gcc && \  
echo "source /openstackinfo/*.sh" >> ~/.bashrc  
  
CMD ["glance", "--version"]  

