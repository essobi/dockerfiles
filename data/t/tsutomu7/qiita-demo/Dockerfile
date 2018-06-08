FROM tsutomu7/alpine-python  
  
RUN conda install -y pillow numexpr && \  
pip install ortoolpy dual simpy && \  
rm -rf /root/.c* /opt/conda/pkgs/*  
EXPOSE 8888  
ADD qiita_demo.tgz /root/  
WORKDIR /root/  
CMD ["sh", "-c", "jupyter notebook --ip=*"]  
  

