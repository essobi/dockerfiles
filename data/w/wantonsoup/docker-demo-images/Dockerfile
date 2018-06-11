# Docker demo image, as used on try.jupyter.org and tmpnb.org  
FROM jupyter/minimal  
  
MAINTAINER Jupyter Project <jupyter@googlegroups.com>  
  
USER root  
  
# Julia dependencies  
RUN apt-get install -y julia libnettle4 && apt-get clean  
  
# R dependencies that conda can't provide (X, fonts)  
RUN apt-get install -y libxrender1 fonts-dejavu && apt-get clean  
  
RUN mkdir /home/wantonsoup-demo  
RUN mkdir /home/wantonsoup-demo/communities  
RUN mkdir /home/wantonsoup-demo/featured  
ADD notebooks/ /home/wantonsoup-demo/  
ADD requirements_python.txt /home/wantonsoup-demo/  
ADD requirements_r.txt /home/wantonsoup-demo/  
  
EXPOSE 8888  
RUN useradd -ms /bin/bash wantonsoup-demo  
  
RUN chown -R wantonsoup-demo:wantonsoup-demo /home/wantonsoup-demo  
  
USER wantonsoup-demo  
ENV HOME /home/wantonsoup-demo  
ENV SHELL /bin/bash  
ENV USER wantonsoup-demo  
ENV PATH $CONDA_DIR/bin:$PATH  
WORKDIR $HOME  
  
USER root  
  
# Python packages  
RUN conda install --yes --file requirements_python.txt && conda clean -yt  
  
# R packages  
RUN conda config --add channels r  
RUN conda install --yes --file requirements_r.txt && conda clean -yt  
  
# IJulia and Julia packages  
RUN julia -e 'Pkg.add("IJulia")'  
RUN julia -e 'Pkg.add("Gadfly")' && julia -e 'Pkg.add("RDatasets")'  
  
# Featured notebooks  
RUN git clone \--depth 1 https://github.com/jvns/pandas-cookbook.git
/home/wantonsoup-demo/featured/pandas-cookbook/  
  
# Convert notebooks to the current format  
RUN find . -name '*.ipynb' -exec ipython nbconvert --to notebook {} --output
{} \;  
RUN find . -name '*.ipynb' -exec ipython trust {} \;  
  
CMD ipython notebook  

