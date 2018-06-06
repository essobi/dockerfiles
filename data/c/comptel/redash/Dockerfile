FROM redash/base:latest  
  
# We first copy only the requirements file, to avoid rebuilding on every file  
# change.  
COPY requirements.txt requirements_dev.txt requirements_all_ds.txt ./  
RUN pip install -r requirements.txt -r requirements_dev.txt -r
requirements_all_ds.txt  
  
COPY . ./  
RUN npm install && npm run build && rm -rf node_modules  
RUN chown -R redash /app  
  
ARG SECRETARY_VERSION=0.10.1  
RUN wget -O /usr/bin/secretary
https://github.com/meltwater/secretary/releases/download/${SECRETARY_VERSION}/secretary-
Linux-x86_64 && \  
chmod +x /usr/bin/secretary  
  
USER redash  
  
ENTRYPOINT ["/app/bin/docker-entrypoint"]  

