FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python-pip \  
python-dev \  
build-essential && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /src  
COPY src/requirements /src/  
WORKDIR /src  
  
RUN pip install -r requirements  
  
COPY src/* /src/  
  
RUN useradd --system --uid 666 -M --shell /usr/sbin/nologin crash-report && \  
chown crash-report -R /src  
  
USER crash-report  
  
EXPOSE 8080  
ENTRYPOINT ["python"]  
CMD ["server.py"]  
  

