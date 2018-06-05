FROM amazonlinux:latest  
  
# Install node and related tools  
ENV NODE_VERSION 8.8.1  
ENV NODE_PATH /root/.nvm/versions/node/v$NODE_VERSION/bin  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash \  
&& . ~/.nvm/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& node -e "console.log('Running Node.js ' + process.version)"  
ENV PATH $NODE_PATH:$PATH  
  
# Install python 3.6 and development tools  
RUN yum -y update \  
&& yum -y upgrade \  
&& yum -y groupinstall "Development Tools" \  
&& yum -y install python36-devel python36-pip gcc  
RUN easy_install-3.6 pip  
  
# Create env directory  
RUN mkdir ~/env  
WORKDIR ~/env  
COPY files/requirements.txt requirements.txt  
RUN pip3 install -r requirements.txt  
  
# Add volume to map to project application  
VOLUME /app  
  
CMD ["/bin/bash"]  

