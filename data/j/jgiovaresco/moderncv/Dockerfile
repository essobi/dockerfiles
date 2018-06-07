  
FROM jgiovaresco/lualatex:latest  
MAINTAINER Julien Giovaresco <dev@giovaresco.fr>  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y wget unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/local/share/texmf/tex/latex && \  
cd /tmp && \  
wget --no-check-certificate
http://mirrors.ctan.org/macros/latex/contrib/moderncv.zip && \  
wget --no-check-certificate http://mirrors.ctan.org/fonts/fontawesome.zip && \  
unzip moderncv.zip -d /usr/local/share/texmf/tex/latex && \  
unzip fontawesome.zip fontawesome/tex/* -d /usr/local/share/texmf/tex/latex &&
\  
mv /usr/local/share/texmf/tex/latex/fontawesome/tex/*
/usr/local/share/texmf/tex/latex/fontawesome/ && \  
rm -r /usr/local/share/texmf/tex/latex/fontawesome/tex/ /tmp/* && \  
cd /usr/local/share/texmf/ && mktexlsr  
  
USER lualatex  
WORKDIR /data  
  
ENTRYPOINT [ "lualatex" ]  
CMD [""]

