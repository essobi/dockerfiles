FROM r-base  
  
RUN apt-get update \  
&& apt-get install -y default-jdk libssl-dev libcurl4-openssl-dev libxml2-dev
\  
python2.7 python-pip libjson-perl  
  
RUN pip install pdfminer  
  
RUN cd /opt \  
&& wget --quiet http://igm.univ-mlv.fr/~unitex/Unitex3.0.zip \  
&& unzip Unitex3.0.zip \  
&& (cd Unitex3.0/Src/C++/build && make install) \  
&& rm Unitex3.0.zip  
  
ENV UNITEX_HOME=/opt/Unitex3.0  
RUN mkdir -p /vespa/R-lib  
ENV R_LIBS_USER=/vespa/R-lib  
  
WORKDIR /vespa  
  
# Les packages dont dépend x.ent, qui ne devraient pas trop bouger  
RUN Rscript -e "install.packages(c('devtools', 'brew', 'colorspace', \  
'dichromat', 'evaluate', 'formatR', 'ggplot2', 'gtable', 'highr', \  
'httpuv', 'knitr', 'labeling', 'markdown', 'munsell', 'opencpu', \  
'plyr', 'RColorBrewer', 'Rcpp', 'reshape2', 'rJava', 'scales', \  
'statmod', 'venneuler', 'xtable', 'yaml'))"  
  
COPY install_x.ent.sh /vespa/  
COPY indexation/ini.json.dist /vespa/indexation/  
  
RUN ./install_x.ent.sh && rm -rf R-lib/x.ent/out  
  
COPY . /vespa  
  
CMD ["make"]  

