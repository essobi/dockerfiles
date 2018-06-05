FROM continuumio/miniconda3  
  
RUN apt-get update \  
&& apt-get install -y \  
nginx && \  
mkdir /data /meta /whoosh  
  
WORKDIR /app  
  
ADD environment.yml /app/environment.yml  
  
ENV PATH /opt/conda/envs/ave2/bin:$PATH  
  
RUN conda update conda -q -y && \  
conda env create -q -f environment.yml  
  
ADD . /app  
  
RUN python setup.py develop && \  
cp settings.docker.cfg settings.cfg && \  
cp nginx.conf /etc/nginx/sites-enabled/default && \  
cd /var/www/html && \  
curl -L 'https://bintray.com/nlesc-ave/ave/download_file?file_path=ave-app-
latest.tar.bz2' | tar -jxf -  
  
CMD service nginx start && gunicorn -w 4 --threads 2 -t 60 -b 127.0.0.1:8080
avedata.app:app  
  
VOLUME /data /meta /whoosh  
EXPOSE 80  

