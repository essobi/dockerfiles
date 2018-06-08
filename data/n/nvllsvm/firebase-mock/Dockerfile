FROM gliderlabs/alpine:3.6  
  
RUN apk \--update add curl python3 && \  
curl -LsSf https://bootstrap.pypa.io/get-pip.py | python3 && \  
pip3 install firebasemock && \  
apk del \--purge curl python3-dev && \  
rm -rf /root/.cache  
  
EXPOSE 8000  
EXPOSE 8001  
EXPOSE 8002  
  
CMD firebasemock  

