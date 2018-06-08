FROM python:2-onbuild  
MAINTAINER Pedro Ferreira <P.E.Ferreira@cwi.nl>  
  
RUN \  
apt-get update && \  
apt-get install -y python-psycopg2 && \  
pip install psycopg2 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY scripts /scripts/  
  
#"/scripts/sensor_cycle.py"  
CMD ["bash"]  

