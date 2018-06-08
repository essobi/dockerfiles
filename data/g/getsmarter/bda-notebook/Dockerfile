FROM jupyter/base-notebook  
  
USER root  
  
# Install apt-get packages  
RUN apt-get update && apt-get install -y \  
nano \  
cron \  
dnsutils \  
build-essential python-dev \  
libfreetype6 libfreetype6-dev libxft-dev \  
graphviz libgraphviz-dev \  
pandoc \  
git \  
mercurial \  
subversion \  
python-pip \  
unzip \  
libav-tools \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Set terminal  
RUN echo 'export TERM=xterm' >> /root/.bashrc && echo 'export TERM=xterm' >>
/home/jovyan/.bashrc  
  
USER $NB_USER  
  
RUN git clone \--branch "master" \--depth 1
https://github.com/getsmarter/bda.git /home/jovyan/bda  
  
USER root  
  
# Install python3 pip packages  
RUN pip install --upgrade pip  
RUN pip install \  
bandicoot==0.5.3 \  
python-louvain==0.3 \  
pandas==0.19.2 \  
numpy==1.11 \  
folium==0.3.0 \  
geocoder==1.38.1 \  
matplotlib==2.2.2 \  
pandas-datareader==0.6.0 \  
wikipedia==1.4.0 \  
tqdm==4.23.1 \  
scipy==1.0.1 \  
scikit-learn==0.19.1 \  
ipykernel==4.8.2 \  
pillow==5.1.0 \  
pygraphviz==1.3.1 \  
graphviz==0.8.3 \  
pydot==1.2.4 \  
pydotplus==2.0.2 \  
git+https://github.com/rasbt/mlxtend.git#egg=mlxtend  
  
# Add jovyan user to sudoers group  
RUN echo "$NB_USER ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers  
  
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/  
RUN chown -R jovyan:users /home/$NB_USER/.jupyter/  
  
COPY startup.sh /usr/local/bin/  
RUN chmod 775 /usr/local/bin/startup.sh  
  
COPY deploy.sh /usr/local/bin/  
RUN chmod 775 /usr/local/bin/deploy.sh  
  
RUN touch /var/log/deploy.log && chmod 666 /var/log/deploy.log  
  
RUN git config --global user.email "jovyan@jupyter.local"  
RUN git config --global user.name "Jovyan"  
  
USER $NB_USER  
  
ENTRYPOINT startup.sh  

