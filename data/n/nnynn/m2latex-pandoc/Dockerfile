FROM tianon/latex  
  
RUN apt-get update && apt-get install -y wget \  
&& wget -c
https://github.com/jgm/pandoc/releases/download/2.1.2/pandoc-2.1.2-linux.tar.gz
\  
&& tar xvzf pandoc-2.1.2-linux.tar.gz \--strip-components 1 -C /usr \  
&& chmod +x /usr/bin/pandoc \  
&& chmod +x /usr/bin/pandoc-citeproc  
  
RUN apt-get install -y python-pip && pip install pandoc-fignos  
RUN apt-get install -y inkscape  

