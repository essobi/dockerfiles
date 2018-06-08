FROM python  
  
RUN \  
pip install --no-cache-dir glances && \  
pip install --no-cache-dir glances[docker]  
  
ENTRYPOINT [ "glances" ]  

