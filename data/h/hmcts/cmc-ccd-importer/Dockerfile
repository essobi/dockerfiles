FROM alpine:3.7  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
RUN apk add --no-cache curl jq  
  
## Add the wait script to the image  
ADD https://github.com/ufoscout/docker-compose-
wait/releases/download/2.0.0/wait /wait  
  
COPY scripts /scripts  
RUN ["chmod", "+x", "/wait"]  
  
RUN chmod +x /scripts/*.sh /scripts/*.py  
RUN pip3 install -r /scripts/requirements.txt  
  
COPY data/CCD_Definition_CMC.template.xlsx /definition-template.xlsx  
  
CMD "/wait" && "/scripts/upload-definition.sh"  

