FROM continuumio/anaconda3  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update -y && \  
apt-get install -y curl && \  
apt-get install -y vim && \  
pip install virtualenv virtualenvwrapper && \  
echo "WORKON_HOME=~/.virtualenvs" >> ~/.bashrc && \  
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

