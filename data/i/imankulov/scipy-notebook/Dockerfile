FROM jupyter/scipy-notebook:latest  
LABEL maintainer="Roman Imankulov <roman.imankulov@gmail.com>"  
  
USER $NB_UID  
RUN conda install --quiet --yes \  
bqplot \  
boto3 \  
mysql-connector-python \  
psycopg2 \  
python-dotenv \  
records \  
redis \  
sqlalchemy \  
python-dotenv \  
pandasql \  
tqdm \  
snakeviz \  
ua-parser \  
qgrid \  
plotly \  
&& pip install geoip2  
  
USER root  
ADD http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
/usr/local/GeoLite2-City.tar.gz  
  
RUN \  
( cd /usr/local/ \  
&& tar xf /usr/local/GeoLite2-City.tar.gz \  
&& mv GeoLite2-City_* GeoLite2 \  
) \  
&& jupyter labextension install \  
jupyterlab_bokeh \  
bqplot \  
qgrid \  
&& apt-get update && apt-get install -yq --no-install-recommends \  
openssh-client \  
less \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
ENV EDITOR=vim  
USER $NB_UID  

