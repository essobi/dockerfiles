FROM python:3.6.2-alpine3.6  
  
RUN : \  
# Update apk  
&& apk update \  
# Install Dependencies  
&& apk --no-cache add \  
libstdc++ \  
# for gcloud  
python2 \  
# Install Packages  
&& apk --no-cache add \  
bash \  
# Install Build Dependencies  
&& apk --no-cache add --virtual .build-deps \  
curl \  
file \  
freetype-dev \  
g++ \  
gcc \  
gfortran \  
git \  
lapack-dev \  
make \  
openssl \  
perl \  
wget \  
# Install Japanese Morphological Analyzers  
&& git clone \  
\--depth=1 \  
https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers.git \  
/usr/local/src/JapaneseTokenizers \  
&& cd /usr/local/src/JapaneseTokenizers \  
&& make install \  
&& make install_neologd \  
&& python setup.py install \  
&& cd \  
&& rm -rf /usr/local/src/JapaneseTokenizers \  
  
# Install Google Cloud SDK  
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
\--quiet \  
# Install Python Packages  
&& pip --no-cache-dir install \  
matplotlib \  
neologdn \  
numpy \  
pandas \  
PyYAML \  
scipy \  
scikit-learn \  
jupyter \  
# Clean Up  
&& apk del .build-deps  
  
ADD jupyter_notebook_config.py /root/.jupyter  
  
EXPOSE 8888  
VOLUME /notebook  
WORKDIR /notebook  
  
CMD jupyter notebook

