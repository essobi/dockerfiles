FROM jenkins:2.3  
  
MAINTAINER Polonio Davide "poloniodavide@gmail.com"  
  
USER root  
  
RUN apt-get update -qq && \  
apt-get install -y make texlive-latex-extra texlive-luatex cm-super texlive-
bibtex-extra latexmk tex4ht texlive-fonts-recommended texlive-lang-italian &&
\  
apt-get clean  
  
RUN apt-get update -qq && \  
apt-get install -y build-essential libssl-dev curl git-core && \  
apt-get clean  
  
RUN apt-get update -qq && \  
apt-get install -y perl libxml-libxml-perl libxml-libxslt-perl libfile-chdir-
perl libautodie-perl && \  
apt-get clean  
  
RUN mkdir /opt/nvm  
RUN chown -R jenkins:jenkins /opt/nvm  
  
USER jenkins  
  
RUN HOME=/opt/nvm && \  
cd $HOME && \  
touch .bashrc && \  
curl -o\- https://raw.githubusercontent.com/creationix/nvm/v0.31.1/install.sh
| bash  
  
COPY wizard.sh /tmp/  
  
RUN /tmp/wizard.sh 4.4.3  

