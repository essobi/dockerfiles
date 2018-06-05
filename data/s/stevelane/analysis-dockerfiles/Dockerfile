FROM stevelane/analysis-dockerfiles:base-2017  
LABEL maintainer="Steve Lane"  
LABEL email="lane.s@unimelb.edu.au"  
  
## Add in tikz support  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
pgf \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
## Add in CEBRA styles  
RUN mkdir -p /home/cebra-templates \  
&& cd /home/cebra-templates \  
&& wget https://bitbucket.org/cebra/cebra-templates/get/master.tar.gz \  
&& tar -xzf master.tar.gz --strip=1 \  
&& mkdir -p /usr/local/share/texmf/tex/latex/cebra \  
&& ln -s /home/cebra-templates/CEBRALogo-01.pdf \  
/usr/local/share/texmf/tex/latex/cebra/CEBRALogo-01.pdf \  
&& ln -s /home/cebra-templates/cebra.sty \  
/usr/local/share/texmf/tex/latex/cebra/cebra.sty \  
&& texhash  
  
# Remove unnecessary tmp files  
RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
## Run ssh by default  
CMD ["/usr/sbin/sshd", "-D"]  

