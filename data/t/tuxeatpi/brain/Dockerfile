FROM python:3.5-alpine  
  
RUN apk add --no-cache git gcc python-dev linux-headers musl-dev  
  
COPY requirements.txt /opt/requirements.txt  
COPY test_requirements.txt /opt/test_requirements.txt  
RUN pip install -r /opt/requirements.txt  
  
RUN mkdir /workdir  
  
COPY setup.py /opt/setup.py  
WORKDIR /opt  
COPY tuxeatpi_brain /opt/tuxeatpi_brain  
RUN python /opt/setup.py install  
  
WORKDIR /workdir  
  
COPY dialogs /dialogs  
COPY intents /intents  
  
ENTRYPOINT ["tep-brain", "-w", "/workdir", "-I", "/intents", "-D", "/dialogs"]  

