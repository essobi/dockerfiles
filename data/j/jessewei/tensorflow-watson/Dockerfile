FROM tensorflow/tensorflow:latest  
  
ENV HOME=/root  
  
#  
# install ijavascript  
#  
# install nodejs  
RUN apt-get update && \  
apt-get -y install nodejs-legacy npm && \  
apt-get clean  
  
# install ijavascript  
RUN npm install -g ijavascript  
  
#&& mv /node_modules ${HOME}/node_modules && npm cache clean  
# prepare kernel.json for ijavascript  
RUN mkdir -p ${HOME}/.ipython/kernels/ijs  
ADD files/ijs/kernel.json ${HOME}/.ipython/kernels/ijs/kernel.json  
  
#  
# Install watson and tools  
#  
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade watson-
developer-cloud wordcloud google-api-python-client  
RUN cd /notebooks && npm install watson-developer-cloud --save && npm install
json-query -g && npm cache clean  
  
#  
# Arrange workspace  
#  
RUN mkdir -p /notebooks/nb_demo/watson && \  
mkdir -p /notebooks/nb_demo/tensorflow && \  
mkdir -p /notebooks/nb_demo/resources  
COPY files/nb_demo /notebooks/nb_demo  

