FROM python:2.7.9  
MAINTAINER John Shen  
  
RUN apt-get update && \  
apt-get install -y liblapack-dev \  
libblas-dev \  
gfortran \  
python-dev && \  
pip install tornado numpy requests  
  
RUN pip install scipy scikit-learn && \  
git clone https://github.com/raphael-group/magi-stat-server.git src  
  
EXPOSE 8888  
CMD ["python", "/src/statserver.py", "--port", "8888"]  
  

