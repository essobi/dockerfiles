# ----------------------  
# Docker's informations:  
# ----------------------  
FROM negetem/python:latest  
MAINTAINER Jocelyn LOPEZ <jocelyn.lopez.pro@gmail.com>  
  
# ----------------  
# Set environment:  
# ----------------  
ENV PYTHON_ROOT=/executables  
ENV PYTHON_WORKING_DIR=/tmp/workdir  
COPY ["api.py", "/api.py"]  
COPY ["requirements.txt", "/requirements.txt"]  
  
# --------------------------  
# Install required packages:  
# --------------------------  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python3 \  
python3-setuptools \  
python3-pip \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip3 install --upgrade pip \  
&& pip3 install setuptools wheel  
RUN pip3 install -r /requirements.txt  
  
# -----------  
# Launch api:  
# -----------  
RUN chmod +x /api.py  
EXPOSE 5000  
CMD /api.py  

