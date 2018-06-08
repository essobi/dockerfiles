FROM python:3.4-jessie  
  
MAINTAINER Sherpany DevOps Team "devops@sherpany.com"  
  
ENV PYTHONUNBUFFERED=1 \  
PIP_REQUIRE_VIRTUALENV=true \  
PIPSI_HOME=/root/.pipsi/venvs \  
PIPSI_BIN_DIR=/root/.pipsi/bin \  
PATH=/virtualenv/bin:/root/.pipsi/bin:$PATH \  
LC_ALL=C.UTF-8 \  
LANG=C.UTF-8  
  
COPY stack /stack/base  
RUN DEBIAN_FRONTEND=noninteractive /stack/base/install.sh  
  
WORKDIR /app  
  
ENTRYPOINT ["/tini", "-g", "--"]  
CMD ["bash"]  

