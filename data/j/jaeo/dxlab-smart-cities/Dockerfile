  
##################################################  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
## Smart Cities Natal 2017  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
##################################################  
  
FROM jaeo/jupyter-spark  
  
#-------------------------------------------------  
# Python dependencies  
#-------------------------------------------------  
  
RUN conda install --yes --quiet \  
folium \  
gmaps \  
ipywidgets \  
pika \  
&& conda clean -tipsy \  
&& jupyter nbextension enable --py --sys-prefix gmaps  
  
  
#-------------------------------------------------  
# Node  
#-------------------------------------------------  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nodejs \  
npm \  
&& ln -s `which nodejs` /usr/bin/node \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
RUN npm install express socket.io rabbit.js  

