FROM tsutomu7/alpine-python  
  
EXPOSE 5000 8888  
WORKDIR /root/  
COPY flask_server.py /root/  
RUN conda install -y pillow numexpr && \  
pip install ortoolpy dual simpy && \  
rm -rf /root/.c* /opt/conda/pkgs/*  
CMD ["python", "flask_server.py"]  
  

