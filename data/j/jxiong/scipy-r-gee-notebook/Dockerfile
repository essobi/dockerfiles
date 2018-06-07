FROM tylere/docker-debian-python3-scipy-notebook  
  
MAINTAINER Jun Xiong <jun.xiong1981@gmail.com>  
  
USER root  
  
RUN echo "deb http://httpredir.debian.org/debian jessie main contrib" >
/etc/apt/sources.list  
RUN echo "deb http://httpredir.debian.org/debian jessie-updates main contrib"
>> /etc/apt/sources.list  
RUN echo "deb http://security.debian.org/ jessie/updates main contrib" >>
/etc/apt/sources.list  
RUN apt-get update  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER jovyan  
  
RUN pip install https://github.com/ipython-
contrib/jupyter_contrib_nbextensions/tarball/master  
RUN jupyter contrib nbextension install --user  
RUN jupyter nbextension enable toc2/main  
RUN jupyter nbextension enable codefolding/main  
RUN pip install qgrid pandas-datareader tabulate shovel  
RUN conda install -y -c r r-base r-essentials rpy2 r-dplyr r-ggplot2  
# RUN conda install -y -c anaconda pytables  
RUN conda install -y -c scitools cartopy  
RUN conda install -y pandoc  
RUN conda install -y graphviz  
RUN conda install -y -c osgeo gdal  
RUN ln -s /opt/conda/lib/libjpeg.so.9 /opt/conda/lib/libjpeg.so.8  

