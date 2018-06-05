FROM python:3.6-slim  
  
COPY requirements.txt /app/  
RUN apt-get -y update && \  
apt-get install -y \  
g++ \  
gcc \  
libgdal1h \  
libgdal-dev \  
libgeos-3.4.2 \  
libgeos-c1 \  
libgeos-dev \  
&& \  
pip install -r /app/requirements.txt && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf ~/.pip && \  
apt remove -y \  
g++ \  
gcc \  
libgdal-dev \  
libgeos-dev \  
&& \  
apt-get autoremove -y  
COPY . /app/  
RUN mkdir /output  
EXPOSE 5002  
VOLUME /data  
VOLUME /output  
ENV TMPDIR=/data  
WORKDIR /output  
ENTRYPOINT ["python", "/app/docker_entrypoint.py"]  
CMD ["--server"]  

