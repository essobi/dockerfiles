FROM ogelp/pyenv  
  
USER python_user  
  
COPY requirements.in requirements.in  
  
RUN \  
for version in $(pyenv versions | cut -c3- | cut -d' ' -f1); do pyenv global
$version && pip-compile && pip-sync && pyenv rehash; done && \  
rm -f requirements.in requirements.txt  
  
CMD ["bash"]  

