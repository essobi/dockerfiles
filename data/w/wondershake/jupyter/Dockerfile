FROM python:3.6.2-alpine3.6  
# Install apk Packages  
RUN apk update \  
# Install Dependencies  
&& apk --no-cache add \  
libstdc++ \  
# Install Utilities  
&& apk --no-cache add \  
bash \  
# Install Build Dependencies  
&& apk --no-cache add \--virtual .build-deps \  
curl \  
file \  
freetype-dev \  
g++ \  
gcc \  
gfortran \  
git \  
lapack-dev \  
libxml2-dev \  
libxslt-dev \  
make \  
openssl \  
perl \  
wget  
  
# Install Japanese Morphological Analyzers  
RUN git clone \  
\--depth=1 \  
https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers.git \  
/usr/local/src/JapaneseTokenizers \  
&& cd /usr/local/src/JapaneseTokenizers \  
&& make install \  
&& make install_neologd \  
&& python setup.py install \  
&& cd \  
&& rm -rf /usr/local/src/JapaneseTokenizers  
  
# Install Google Cloud SDK  
RUN apk --update --no-cache add python2 \  
&& mkdir /opt \  
&& curl -o /opt/google-cloud-sdk.tar.gz \  
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-158.0.0-linux-x86_64.tar.gz \  
&& cd /opt \  
&& tar zxf google-cloud-sdk.tar.gz \  
&& rm google-cloud-sdk.tar.gz \  
&& CLOUDSDK_PYTHON=$(which python2) \  
google-cloud-sdk/install.sh \  
\--usage-reporting=false \  
\--rc-path=/etc/profile.d/gcloud.sh \  
\--quiet  
  
# Install Python Packages  
RUN pip --no-cache-dir install PyYAML  
RUN pip --no-cache-dir install gensim  
RUN pip --no-cache-dir install inflection  
RUN pip --no-cache-dir install jupyter  
RUN pip --no-cache-dir install matplotlib  
RUN pip --no-cache-dir install neologdn  
RUN pip --no-cache-dir install numpy  
RUN pip --no-cache-dir install pandas  
RUN pip --no-cache-dir install pandas_gbq  
RUN pip --no-cache-dir install scikit-learn  
RUN pip --no-cache-dir install scipy  
RUN pip --no-cache-dir install tqdm  
  
# Make Directories  
RUN mkdir /notebook  
  
# Configure Jupyter Notebook  
ADD jupyter_notebook_config.py /root/.jupyter/  
  
# Enable jupyter_contrib_nbextensions  
# https://github.com/ipython-contrib/jupyter_contrib_nbextensions  
# https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator  
RUN pip --no-cache-dir install jupyter_contrib_nbextensions \  
&& jupyter contrib nbextension install --user \  
&& pip --no-cache-dir install jupyter_nbextensions_configurator \  
&& jupyter nbextensions_configurator enable \--user  
  
# Install font for Japanese (using matplotlib)  
RUN mkdir -p /usr/share/fonts  
COPY IPAGothic /usr/share/fonts/IPAGothic  
RUN fc-cache -fv  
  
# Ports  
EXPOSE 8888  
# Volumes  
VOLUME /notebook  
VOLUME /root/.config/gcloud  
  
WORKDIR /notebook  
CMD jupyter notebook  

