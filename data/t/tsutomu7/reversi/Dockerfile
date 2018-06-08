FROM tsutomu7/alpine-python:blank  
  
RUN apk add --no-cache libstdc++ && \  
conda install -y nomkl numpy jupyter && \  
rm -rf /root/.[acpw]* /opt/conda/pkgs/*  
WORKDIR /root/  
COPY reversi.py reversi.ipynb /root/  
CMD ["sh", "-c", "jupyter notebook --ip=*"]  

