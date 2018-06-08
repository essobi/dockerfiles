FROM alpine:3.3  
RUN apk add --no-cache python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
rm -r /root/.cache  
  
EXPOSE 8001  
WORKDIR /serviceApp  
ADD ./serviceApp /serviceApp  
  
RUN pip install -r /serviceApp/requirements.txt  
  
CMD python /serviceApp/serviceApp.py  
  

