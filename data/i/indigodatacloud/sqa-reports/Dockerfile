FROM ubuntu:xenial  
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>  
  
USER root  
  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get -y install vim texlive texlive-latex-extra python-dev python-pip
libjpeg8-dev zlib1g-dev libtiff5-dev  
RUN apt-get -y install git  
RUN apt-get -y install coreutils  
  
ADD https://raw.githubusercontent.com/amix/vimrc/master/vimrcs/basic.vim
/root/.vimrc  
  
RUN git clone https://github.com/indigo-dc/sqa-reports /srv/sqa-reports  
WORKDIR /srv/sqa-reports/  
RUN pip install -r requirements.txt  
#RUN python generate_reports.py templates/report.tex specs/accounting.yaml
--output-dir=/srv/sqa-reports/build  

