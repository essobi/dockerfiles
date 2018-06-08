FROM python:2.7  
MAINTAINER Daniel Siepmann  
LABEL Description="This image is used to ease Documentation rendering with
Sphinx." Vendor="DanielSiepmann" Version="1.0"  
  
RUN pip install 'sphinx == 1.6.3' 'sphinx_rtd_theme == 0.2'
'guzzle_sphinx_theme == 0.7'  
  
RUN cd /usr/local/lib/python2.7/site-packages/pygments/lexers/ && \  
wget https://raw.githubusercontent.com/Tuurlijk/Pygments-TypoScript-
Lexer/master/typoscript.py && \  
python _mapping.py  
  
WORKDIR /sphinx  
  
CMD ["make", "html"]  

