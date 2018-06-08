FROM jenkins/jnlp-slave:alpine  
MAINTAINER mecodia GmbH  
  
USER root  
RUN apk update && apk add python3  
RUN pip3 install --no-cache-dir \  
flake8 \  
flake8-blind-except \  
flake8-builtins \  
flake8-colors \  
flake8-comprehensions \  
flake8-docstrings \  
flake8-import-order \  
flake8-mutable \  
flake8-pep3101 \  
flake8-pyi \  
flake8-quotes \  
flake8-string-format \  
pep8-naming  
  
USER jenkins  

