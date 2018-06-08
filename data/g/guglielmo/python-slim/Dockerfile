FROM python:3.6-slim  
  
COPY locales.txt /etc/locale.gen  
  
# provisioning, with gdal  
RUN apt-get -qq update \  
&& apt-get install -y --no-install-recommends \  
wget git-core tmux vim locales less \  
binutils libproj-dev gdal-bin \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo 'alias ll="ls -l"' >> ~/.bashrc \  
&& echo 'alias la="ls -la"' >> ~/.bashrc \  
&& locale-gen  
  
# upgrade pip  
RUN pip3 install --upgrade pip  
  
# initialize app  
RUN mkdir -p /app  
WORKDIR /app  
  

