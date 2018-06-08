FROM python:2.7.12  
ENV PROJECT_VERSION=0.2.2  
WORKDIR /opt/marble  
COPY . /opt/marble/  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
VOLUME ["/opt/bitwrap", "/data"]  
  
ENV BITWRAP_REPO_PATH=/data/  
ENV PNML_PATH=/opt/marble/pnml/  
ENV BITWRAP_PORT=8080  
ENTRYPOINT ["/opt/marble/entry.sh"]  

