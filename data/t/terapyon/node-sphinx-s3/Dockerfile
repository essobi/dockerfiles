FROM terapyon/sphinx-s3  
MAINTAINER "Manabu TERADA" <terada@cmscom.jp>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update -y  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash  
RUN export NVM_DIR="/root/.nvm" && \  
source /root/.bashrc && \  
cd /root && \  
nvm install v6.9.1 && \  
nvm use v6.9.1 && \  
npm -g install gulp  
  
#CMD ["/bin/bash"]  

