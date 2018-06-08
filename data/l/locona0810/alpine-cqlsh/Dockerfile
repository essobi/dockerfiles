FROM alpine:3.6  
RUN apk add --update \  
bash \  
curl \  
py-pip  
  
RUN bash -c "python <(curl https://bootstrap.pypa.io/get-pip.py)"; \  
pip install cqlsh && \  
mkdir /root/.cassandra  
  
COPY ["./cassandra/cqlshrc", "/root/.cassandra/cqlshrc"]  

