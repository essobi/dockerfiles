FROM tsutomu7/python-opencv  
  
ADD picntu.tgz /root/  
RUN pip install --no-cache-dir unionfind && \  
conda install -y flask && \  
mkdir /root/static && \  
rm -rf /root/.c* /opt/conda/pkgs/*  
EXPOSE 5000  
WORKDIR /root  
CMD ["python", "runserver.py"]  
  

