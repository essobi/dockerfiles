FROM ubuntu:xenial  
  
USER root  
  
#install dependencies including librados for python (experimental, downloaded
- this forces to amd64 arch)  
RUN apt-get update &&\  
apt-get install -y git nginx python python-flask python-ceph librados2
librados-dev python-ceph python-pip && \  
pip install --upgrade pip jsonschema flask && \  
git clone https://github.com/Crapworks/ceph-dash  
  
#read InfluxDB endpoint and database from environment variable  
  
#read monitor to connect to from environment variable  
  
#change port the application listens on  
#RUN sed -i -e s/app.run(host='0.0.0.0', debug=True)/app.run(host='0.0.0.0',
port=$PORT debug=True)/ ceph-dash.py  
  
WORKDIR ceph-dash  
  
CMD python ceph-dash.py  

