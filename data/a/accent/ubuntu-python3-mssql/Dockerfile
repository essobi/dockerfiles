FROM ubuntu:16.04  
# apt-get and system utilities  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
apt-transport-https \  
build-essential \  
curl \  
debconf-utils \  
gcc \  
g++-5 \  
software-properties-common \  
wget  
  
# adding custom MS repository  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
# install SQL Server drivers  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y --no-install-recommends
\  
msodbcsql \  
unixodbc-dev  
  
# install SQL Server tools  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y --no-install-recommends
\  
mssql-tools  
  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
RUN /bin/bash -c "source ~/.bashrc"  
  
# install necessary locales  
RUN apt-get update && apt-get install -y --no-install-recommends \  
locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen  
  
# install additional utilities  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gettext \  
nano \  
vim  
  
# python libraries  
RUN add-apt-repository ppa:jonathonf/python-3.6 \  
&& apt-get update && apt-get install -y --no-install-recommends \  
python3.6 \  
python3.6-dev \  
python3.6-venv \  
&& ln -sf /usr/bin/python3.6 /usr/local/bin/python3  
  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& python3.6 get-pip.py \  
&& ln -sf /usr/local/bin/pip /usr/local/bin/pip3  
  
# delete all the apt list files since they're big and get stale quickly  
RUN rm -rf /var/lib/apt/lists/*  
  
# override this accordingly  
CMD ["python3"]

