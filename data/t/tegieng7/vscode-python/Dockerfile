# Visual Studio Code + Python  
FROM tegieng7/vscode  
  
RUN apt-get update && apt-get -y install \  
\--no-install-recommends \  
python \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip  
RUN pip install setuptools  
RUN pip install pylint pep8 autopep8 pydocstyle  
  
RUN ${VSCODE} \--install-extension ms-python.python  
RUN ${VSCODE} \--install-extension njpwerner.autodocstring  
  
ADD utils/settings.json /code/config/User  
RUN chown -R ${USERNAME}:${USERNAME} /code  
  

