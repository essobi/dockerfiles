# base image  
FROM matbloch/dlib-torch  
  
# File Author / Maintainer  
MAINTAINER Matthias Bloch  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
graphicsmagick \  
libssl-dev \  
libffi-dev \  
python-dev \  
python-pip \  
python-numpy \  
python-nose \  
python-scipy \  
python-pandas \  
python-protobuf \  
python-openssl \  
wget \  
zip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
############################################################  
# Install OpenFace  
############################################################  
  
RUN git clone https://github.com/cmusatyalab/openface.git /root/openface
--recursive  
  
RUN python -m pip install --upgrade --force pip  
  
RUN cd /root/openface && \  
./models/get-models.sh && \  
pip2 install -r requirements.txt && \  
python2 setup.py install && \  
pip2 install --user --ignore-installed -r demos/web/requirements.txt && \  
pip2 install -r training/requirements.txt  
  
############################################################  
# Build Identification Node Container  
############################################################  
# Copy the application folder inside the container  
ADD . /uids  
  
ENV PYTHONPATH $PYTHONPATH:/uids  
ENV PATH $PATH:~/torch/install/bin  
  
# install requirements  
RUN cd /uids && \  
pip2 install -r requirements.txt  
  
# inform about port listening (use -p when you start the container)  
EXPOSE 8080 8080  
# download detection models  
CMD /bin/bash -l -c '/uids/models/get-models.sh'  
# Set the default directory where CMD will execute  
WORKDIR /uids  
  
# Start server with custom port listening  
# CMD ["python", "server.py", "-p 8080"]

