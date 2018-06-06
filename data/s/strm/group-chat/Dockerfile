FROM debian:9.2  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libyaml-dev \  
python-pip \  
python-dev \  
build-essential && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /src && \  
mkdir /data  
  
COPY src/requirements /src/  
WORKDIR /src  
  
RUN pip install -r requirements  
  
COPY src/* /src/  
  
RUN useradd --system --uid 666 -M --shell /usr/sbin/nologin group-chat && \  
chown group-chat -R /src && \  
chown group-chat -R /data  
USER group-chat  
  
EXPOSE 8080  
VOLUME /data  
  
ENTRYPOINT ["python"]  
CMD ["server.py"]  

