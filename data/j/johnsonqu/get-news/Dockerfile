FROM tiangolo/uwsgi-nginx-flask:python3.6  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
RUN export PATH=/root/anaconda3/bin:$PATH  
  
ENV LISTEN_PORT 5002  
COPY ./api/api.py /app/main.py  
COPY ./requirements.txt /api/requirements.txt  
COPY ./getnews /getnews  
  
RUN pip install -r /api/requirements.txt  
  
EXPOSE 5002

