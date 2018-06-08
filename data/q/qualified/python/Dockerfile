FROM python:2.7.14-stretch  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libblas-dev \  
liblapack-dev \  
gfortran \  
# For gmpy2  
libgmp-dev \  
libmpc-dev \  
libmpfr-dev \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
RUN set -ex; \  
pip install --no-cache-dir \  
# Scientific: Science  
# A fundamental package for scientific computing with Python.  
numpy==1.12.0 \  
# A Python-based ecosystem of open-source software for mathematics, science,
and engineering.  
scipy==0.13.3 \  
# The most popular Python library for Machine Learning.  
scikit-learn==0.18.1 \  
gmpy2==2.0.2 \  
# Scientific: Data Analysis  
# A library providing high-performance, easy-to-use data structures and data
analysis tools.  
pandas==0.13.1 \  
# Compatibility  
# Python 2 and 3 compatibility utilities  
six==1.10.0 \  
# Database Drivers  
# The official Python client for MongoDB.  
pymongo==3.4.0 \  
# The Redis Python Client.  
redis==2.10.5 \  
# The most popular PostgreSQL adapter for Python.  
psycopg2==2.7 \  
# HTML/XML Manipulation  
# Providing Pythonic idioms for iterating, searching, and modifying HTML or
XML.  
beautifulsoup4==4.2.1 \  
# Python HTTP for Humans.  
requests==2.7.0 \  
# Python Cryptography Toolkit  
pycrypto==2.6.1 \  
;  
  
WORKDIR /workspace  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
PYTHONIOENCODING=UTF-8 \  
PYTHONPATH=/runner/frameworks/python  

