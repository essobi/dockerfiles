# Visual Studio Code + Python  
FROM tegieng7/vscode  
  
RUN apt-get update && apt-get -y install \  
\--no-install-recommends \  
python \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip  
RUN pip install setuptools  
RUN pip install sphinx sphinx_rtd_theme  
  
RUN ${VSCODE} \--install-extension lextudio.restructuredtext \  
&& chown -R ${USERNAME}:${USERNAME} /code  
  

