# Distributed under the terms of the Modified BSD License.  
FROM intelligencelab/datascience_ape:latest  
  
LABEL maintainer "haobibo@gmail.com"  
  
USER root  
  
COPY work /tmp/work/  
# Install data science enviroment: Python/R packages, and related lib
dependencies.  
RUN cd /tmp && apt-get -y update --fix-missing \  
&& apt-get -qq install -y --no-install-recommends `cat
/tmp/work/install_apt.list | cut -d '#' -f 1` \  
&& apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& ( if [ `arch` = "x86_64" ]; then conda install -yq mkl; fi ) \  
&& pip_install_file() { cat $2 | cut -d "%" -f 1 | sed '/^$/d' | xargs -n1 pip
install -U --pre $1; } \  
&& ( npm install --global yarn \  
& R -e
"install.packages(scan('/tmp/work/install_R.list','c'),quiet=T,clean=T)" \  
& ( conda install -yq --file /tmp/work/install_conda.list || true) \  
& pip_install_file -q /tmp/work/install_pip3.list \  
& wait ) \  
&& conda clean -ya \  
&& echo "@ Version of installed Conda packages:" && conda info && conda list |
grep -v "<pip>" \  
&& echo "@ Version of installed Python packages:" && pip list \  
&& echo "@ Version of installed R libraries:" && R -e
"R.Version()\$version.string;installed.packages()[,c(3,10)]" \  
&& ipcluster nbextension enable \  
&& jupyter serverextension enable --sys-prefix --py ipyparallel \  
&& jupyter nbextension install --sys-prefix --py ipyparallel \  
&& jupyter nbextension enable --sys-prefix --py ipyparallel \  
&& jupyter nbextensions_configurator enable --sys-prefix \  
&& jupyter contrib nbextension install --sys-prefix \  
&& jupyter labextension install \  
@jupyterlab/fasta-extension @jupyterlab/geojson-extension @jupyterlab/plotly-
extension @jupyterlab/vega2-extension \  
beakerx-jupyterlab \  
&& jupyter lab build \  
&& ( rm -rf /root/.* /tmp/.* /tmp/* || true ) && cd \  
&& echo "@ Jupyter Extension list" && jupyter nbextension list && jupyter
serverextension list && jupyter labextension list \  
&& echo "@ Version of image: building finished at:" `date`  

