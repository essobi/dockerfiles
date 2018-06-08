FROM linarotechnologies/alpine:edge  
  
RUN apk add --no-cache py-pip python-dev python gcc libc-dev libffi-dev
openssl-dev  
  
RUN pip install pyota  
  
COPY tangle.py /root/tangle.py  
  
CMD cd /root && python tangle.py $@  

