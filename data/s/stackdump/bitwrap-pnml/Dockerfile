FROM python:2.7.12  
ENV PROJECT_VERSION=0.3.0  
WORKDIR /opt/bitwrap-pnml  
COPY . /opt/bitwrap-pnml/  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
VOLUME ["/opt/bitwrap", "/repo"]  
  
ENV BITWRAP_REPO_PATH=/repo/  
ENV BITWRAP_PORT=8080  
ENTRYPOINT ["/opt/bitwrap-pnml/entry.sh"]  

