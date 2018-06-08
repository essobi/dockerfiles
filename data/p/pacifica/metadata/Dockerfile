FROM python:3  
WORKDIR /usr/src/app  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
RUN pip install --no-cache-dir uwsgi  
COPY . .  
EXPOSE 8121  
ENTRYPOINT [ "/bin/bash", "/usr/src/app/entrypoint.sh" ]  

