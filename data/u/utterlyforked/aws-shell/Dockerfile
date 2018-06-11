FROM alpine:latest  
  
RUN \  
mkdir -p /aws && \  
apk -Uuv add --no-cache python3 groff less && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
rm -r /root/.cache && \  
pip install aws-shell  
  
WORKDIR /aws  
ENTRYPOINT ["aws-shell"]  

