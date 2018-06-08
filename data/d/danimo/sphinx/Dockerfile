FROM ubuntu:15.10  
ENV REFRESHED_AT 20160308  
RUN apt update  
RUN apt install -y python-pip  
RUN apt install -y texlive texlive-latex-recommended texlive-latex-extra
texlive-fonts-recommended texlive-lang*  
RUN apt install -y git wget  
RUN apt install -y python-sphinx  
#RUN pip install sphinx_bootstrap_theme  
RUN apt install -y python-sphinxcontrib.phpdomain  
RUN apt install -y python-reportlab  
RUN apt install -y rst2pdf  
RUN adduser --disabled-password --gecos "" jenkins  

