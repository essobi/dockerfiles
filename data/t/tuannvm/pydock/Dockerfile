FROM python:2-alpine  
  
MAINTAINER Tuan Nguyen <me@tuannvm.com>  
  
LABEL Name=pydock  
LABEL Version=1.0.0  
  
ENV WORKDIR /srv  
ENV CERTSDIR /srv/certs  
ENV CA_FILE=${CERTSDIR}/ca.pem  
ENV CLIENT_CERT ${CERTSDIR}/cert.pem  
ENV CLIENT_KEY ${CERTSDIR}/key.pem  
WORKDIR ${WORKDIR}  
  
COPY requirements_alpine.txt requirements.txt  
  
RUN pip install -r requirements.txt  
  
COPY app.py .  
  
ENTRYPOINT ["python", "app.py"]

