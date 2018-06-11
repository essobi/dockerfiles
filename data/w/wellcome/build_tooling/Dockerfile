FROM wellcome/python3  
  
LABEL maintainer = "Wellcome Digital Platform team
<wellcomedigitalplatform@wellcome.ac.uk>"  
LABEL description = "Python build tooling base image"  
  
RUN apk update && apk add git docker bash openssh openssl  
  
COPY requirements.txt /requirements.txt  
RUN pip3 install -r /requirements.txt  
  
VOLUME /data  
WORKDIR /data  
  
COPY tooling.py /builds/tooling.py

