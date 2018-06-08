FROM lucidfrontier45/miniconda:stretch  
LABEL maintainer="Shiqiao Du <lucidfrontier.45@gmail.com>"  
  
RUN set -ex \  
&& conda_pkgs=' \  
nomkl \  
scikit-learn \  
pandas \  
' \  
&& conda install -y $conda_pkgs \  
&& conda clean -i -l -t -y  
  
RUN pip install --no-cache-dir lightgbm  

