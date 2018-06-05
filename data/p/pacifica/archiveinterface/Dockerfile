from python:2  
WORKDIR /usr/src/app  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
RUN pip install --no-cache-dir uwsgi  
COPY . .  
RUN python ./setup.py install  
ENV PAI_BACKEND_TYPE posix  
ENV PACIFICA_AAPI_ADDRESS 0.0.0.0  
ENV PACIFICA_AAPI_PORT 8080  
ENV PAI_PREFIX /srv  
ENTRYPOINT [ "/bin/bash", "/usr/src/app/entrypoint.sh" ]  

