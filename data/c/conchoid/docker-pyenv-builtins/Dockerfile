FROM conchoid/docker-pyenv:v1.1.5-10-2.7-alpine3.6  
  
RUN set -x \  
&& PYTHON2_VERSION="2.7.14" \  
&& PYTHON34_VERSION="3.4.7" \  
&& PYTHON35_VERSION="3.5.4" \  
&& PYTHON36_VERSION="3.6.3" \  
&& pyenv install "$PYTHON2_VERSION" \  
&& pyenv install "$PYTHON34_VERSION" \  
&& pyenv install "$PYTHON35_VERSION" \  
&& pyenv install "$PYTHON36_VERSION" \  
&& pyenv global system "$PYTHON2_VERSION" "$PYTHON36_VERSION"
"$PYTHON35_VERSION" "$PYTHON34_VERSION"  

