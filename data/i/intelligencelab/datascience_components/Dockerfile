# Distributed under the terms of the Modified BSD License.  
FROM intelligencelab/datascience_base:latest  
  
LABEL maintainer "haobibo@gmail.com"  
  
USER root  
  
COPY work /tmp/work/  
  
# Install LaTex and related tools  
RUN cd /tmp && apt-get -y update --fix-missing \  
&& apt-get -qq install -y --no-install-recommends `cat
/tmp/work/install_apt.list | cut -d '#' -f 1` \  
&& apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& pip_install_file() { cat $2 | cut -d "%" -f 1 | sed '/^$/d' | xargs -n1 pip
install -U --pre $1; } \  
&& pip_install_file -q /tmp/work/install_pip3.list \  
&& echo "@ Version of installed Conda packages:" && conda info && conda list |
grep -v "<pip>" \  
&& echo "@ Version of installed Python packages:" && pip list \  
&& echo "@ Version of installed R libraries:" && R -e
"R.Version()\$version.string;installed.packages()[,c(3,10)]" \  
&& jupyter labextension install @jupyterlab/latex \  
&& jupyter lab build \  
&& ( rm -rf /root/.* /tmp/.* /tmp/* || true ) && cd \  
&& echo "@ Jupyter Extension list" && jupyter nbextension list && jupyter
serverextension list && jupyter labextension list \  
&& echo "@ Version of image: building finished at:" `date`  
  

