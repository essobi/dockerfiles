FROM continuumio/miniconda3  
MAINTAINER vsochat@stanford.edu  
  
# docker build -t vanessa/tunel .  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN apt-get update  
RUN apt-get -y install build-essential  
RUN apt-get -y install apt-utils cmake wget unzip libffi-dev libssl-dev \  
libtool autotools-dev automake autoconf git \  
libarchive-dev squashfs-tools uuid-dev \  
vim jq aria2 nginx  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Install Globus Personal Connect  
WORKDIR /opt  
RUN wget
https://s3.amazonaws.com/connect.globusonline.org/linux/stable/globusconnectpersonal-2.3.4.tgz
&& \  
tar xzf globusconnectpersonal-2.3.4.tgz && mv globusconnectpersonal-2.3.4
globus && sed -i -e 's/-eq 0/-eq 999/g' /opt/globus/globusconnectpersonal  
  
RUN git clone https://github.com/sirosen/globusconnectpersonal-py3-patched &&
\  
cp globusconnectpersonal-py3-patched/gc*.py /opt/globus  
  
#RUN git clone -b development-2.x
https://github.com/singularityware/singularity.git \  
RUN git clone -b token-sanity https://github.com/dctrud/singularity.git \  
&& cd singularity && ./autogen.sh && ./configure --prefix=/usr/local \  
&& make && make install  
  
ADD . /code  
  
# Set up nginx  
RUN cp /code/script/nginx.conf /etc/nginx/nginx.conf && \  
cp /code/script/nginx.gunicorn.conf /etc/nginx/sites-enabled/default && \  
chmod u+x /code/script/entrypoint.sh && \  
cp /code/tunel/config_dummy.py /code/tunel/config.py && \  
chmod u+x /code/script/generate_key.sh && \  
/bin/bash /code/script/generate_key.sh /code/tunel/config.py  
  
WORKDIR /code  
RUN /opt/conda/bin/pip install --upgrade pip && \  
/opt/conda/bin/pip install globus-cli && \  
/opt/conda/bin/pip install -r /code/requirements.txt && \  
/opt/conda/bin/pip install sregistry==0.0.83 && \  
/opt/conda/bin/pip install spython==0.0.29 && \  
/opt/conda/bin/python setup.py install && \  
ln -s /opt/conda/bin/python /usr/bin/python  
  
# Clean up  
RUN apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add a user for Globus, etc.  
RUN useradd -ms /bin/bash tunel-user  
RUN echo "gtunel-user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
ENTRYPOINT ["/bin/bash", "/code/script/entrypoint.sh"]  
WORKDIR /code  
EXPOSE 5000  
EXPOSE 80  

