FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
ENV HOUSTON_URL=http://houston ALPHALENS_VERSION=0.3.2 SHELL=/bin/bash \  
YOU_ARE_INSIDE_JUPYTER=true MOONSHOT_CACHE_DIR=/codeload/tmp  
  
# Install ta-lib  
# (zip is for backups)  
RUN apt-get -y update && apt-get -y install \  
zip \  
build-essential \  
libfreetype6-dev \  
libpng-dev \  
libopenblas-dev \  
liblapack-dev \  
gfortran \  
&& cd /tmp \  
&& curl -L https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-
lib-0.4.0-src.tar.gz | tar xvz \  
&& cd ta-lib \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& pip install TA-Lib==0.4.16 \  
&& cd /tmp \  
&& rm -r ta-lib  
  
RUN /bin/bash -c "source activate /opt/conda" \  
&& pip install https://codeload.github.com/quantrocket-
llc/pyfolio/zip/qr0.8.0.1 \  
&& pip install theano==0.9.0 \  
&& pip install pymc3==3.1 \  
&& pip install
https://codeload.github.com/quantopian/alphalens/zip/v${ALPHALENS_VERSION} \  
&& pip install jupyter==1.0.0 \  
&& pip install jupyterlab==0.31.8 \  
&& pip install notebook==5.4.0 \  
&& pip install -U quantrocket-client \  
&& pip install argcomplete \  
&& pip install quantrocket-moonchart \  
&& pip install quantrocket-moonshot \  
&& /bin/bash -c "source deactivate" \  
&& apt-get update && apt-get install -y g++ # install g++ for theano  
  
RUN conda install -c conda-forge nodejs \  
&& jupyter labextension install @quantrocket/jupyterlab_quantrocket_ibgui \  
&& npm install -g json2yaml  
  
COPY bashrc /root/.bashrc  
COPY startup /root/.ipython/profile_default/startup  
  
EXPOSE 80  
# this service is proxied by houston, so we enable CORS and disable  
# authentication (since houston provides Basic Auth for cloud deployments);  
# NOTE: NO PORTS SHOULD BE PUBLISHED FOR THIS SERVICE  
CMD ["jupyter", "notebook", "-y", "--allow-root", "--no-browser", \  
"--notebook-dir=/codeload", "--NotebookApp.token=''", \  
"--ip=0.0.0.0", "--port=80", "--port-retries=0", \  
"--NotebookApp.allow_origin=*", \  
"--NotebookApp.base_url=/jupyter"]  

