FROM tensorflow/tensorflow:1.6.0-gpu-py3  
MAINTAINER notname "notname@gmail.com"  
ENV data /data  
ENV reponame notnamegg-tensorflow-Distributed-training  
WORKDIR ${data}  
# Update aptitude with new repo  
RUN apt-get update  
  
# Install software  
RUN apt-get install -y git  
# Make ssh dir  
RUN mkdir /root/.ssh/  
  
# Copy over private key, and set permissions  
RUN apt-get -y install openssh-client protobuf-compiler vim psmisc python3-tk
wget  
RUN ssh-keygen -q -t rsa -N '' -f /root/.ssh/id_rsa  
  
# Create known_hosts  
RUN touch /root/.ssh/known_hosts  
# Generate ssh key  
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
# clone latest code  
RUN username=$(whoami) && git config --global user.email
"${username}@github.com"  
RUN username=$(whoami) && git config --global user.name "${username}"  
RUN git config --global push.default simple  
RUN git clone https://github.com/notnamegg/${reponame}.git  
RUN cd ${reponame} && git submodule init  
RUN cd ${reponame} && git submodule update  
RUN pip install cython  
RUN cd ${reponame}/cocoapi/PythonAPI && make && make install && python
setup.py install  
RUN cd ${reponame}/models && git remote add github
https://github.com/notnamegg/tensorflow-model.git  
RUN cd ${reponame}/models && git branch r1.6 && git checkout r1.6  
RUN cd ${reponame}/models && git fetch github  
RUN cd ${reponame}/models && git pull github r1.6  
# install object_detection  
RUN cd ${reponame}/models/research && protoc object_detection/protos/*.proto
--python_out=.  
RUN echo "export RESEARCHPATH=${data}/${reponame}/models/research" >>
/root/.bashrc  
RUN echo 'export PYTHONPATH=$PYTHONPATH:$RESEARCHPATH:$RESEARCHPATH/slim' >>
/root/.bashrc  
  
EXPOSE 3000  
EXPOSE 3001  
EXPOSE 3002  

