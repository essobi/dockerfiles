FROM ubuntu:14.04  
MAINTAINER Francesco Marconi <francesco.marconi@polimi.it>  
  
# Setting the environment  
ENV USERHOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
ENV Z3_VERSION 4.5.0  
WORKDIR /tmp  
# Update the repos and install all the used packages  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
unzip \  
xorg \  
gcc \  
g++ \  
make \  
git \  
python \  
python-dev \  
python-distribute \  
# python-pip \  
python-tk \  
# python-matplotlib \  
sbcl \  
zlib1g-dev \  
curl && \  
# dependencies needed for matplotlib  
apt-get build-dep -y --force-yes python-matplotlib && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# installing minisat  
RUN curl -L http://minisat.se/downloads/minisat-2.2.0.tar.gz -o
/tmp/minisat-2.2.0.tar.gz  
WORKDIR /tmp  
RUN tar -xvzf minisat-2.2.0.tar.gz && \  
export MROOT=/tmp/minisat &&\  
cd minisat/core/ && \  
make && \  
cp minisat /usr/local/bin/minisat  
  
# installing z3  
RUN curl -L
https://github.com/Z3Prover/z3/releases/download/z3-${Z3_VERSION}/z3-${Z3_VERSION}-x64-ubuntu-14.04.zip
-o /tmp/z3.zip \  
&& unzip /tmp/z3.zip -d /tmp \  
&& cp /tmp/z3-${Z3_VERSION}-x64-ubuntu-14.04/bin/z3 /usr/local/bin/z3 \  
&& chmod a+x /usr/local/bin/z3  
  
# installing zot  
RUN git clone https://github.com/fm-polimi/zot /usr/local/zot/ && \  
ln -s /usr/local/zot/asdfs/*.asd /usr/lib/sbcl/site-systems/ && \  
cp /usr/local/zot/bin/zot /usr/local/bin/  
  
#installing pip  
WORKDIR /tmp  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
#environment variables for D-VerT  
ENV PROJECT_FOLDER /opt/DICE-Verification/  
ENV SERVER_CODE_FOLDER ${PROJECT_FOLDER}d-vert-server/  
# ENV FORMAL_DICE ${SERVER_CODE_FOLDER}json2mc/  
# ENV FORMAL_DICE ${SERVER_CODE_FOLDER}d-vert-json2mc/json2mc  
ENV JSON2MC_FOLDER ${SERVER_CODE_FOLDER}d-vert-json2mc/  
  
# get D-VerT from github  
# RUN git clone https://github.com/dice-project/DICE-Verification
$PROJECT_FOLDER  
# load code from current directory  
ADD . $SERVER_CODE_FOLDER  
  
# Install and setup virtualenv  
RUN pip install virtualenv  
WORKDIR $PROJECT_FOLDER  
RUN virtualenv -p /usr/bin/python2.7 venv  
RUN ["/bin/bash", "-c", "source venv/bin/activate"]  
#load all needed packages from pip  
RUN pip install -r ${SERVER_CODE_FOLDER}requirements.txt  
  
# install json2mc via pip  
WORKDIR $JSON2MC_FOLDER  
RUN pip install .  
  
#apply modifications to zot  
# WORKDIR $SERVER_CODE_FOLDER  
# RUN cp zot_changes/* /usr/local/zot/asdfs  
# add user to run celery worker as non-root user  
RUN adduser --disabled-password --gecos '' celery-user && adduser celery-user
sudo && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
RUN chown -R celery-user ${SERVER_CODE_FOLDER}static/  
# move to the server code folder  
WORKDIR $SERVER_CODE_FOLDER  
  
CMD ["bash"]  
  

