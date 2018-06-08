FROM ubuntu:latest  
MAINTAINER phil schatzmann  
RUN apt-get update && apt-get install -y gcc g++ pandoc texlive-xetex bzip2
git curl && apt-get clean  
  
# Node  
WORKDIR /opt  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && apt-get install
-y nodejs  
  
# Miniconda  
WORKDIR /opt  
ADD https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
/opt/install.sh  
RUN chmod +x /opt/install.sh && /opt/install.sh -b  
ENV PATH=/root/miniconda3/bin:${PATH}  
  
# Jupyterlab  
RUN conda config --add channels anaconda --add channels conda-forge --add
channels anaconda-cluster --add channels cyclus \  
&& conda install -y pip virtualenv pandas requests psycopg2 statsmodels pystan
fbprophet tensorflow keras scipy jupyter scikit-learn matplotlib pillow
seaborn nltk gensim plotly traittypes pytest scala java-jdk maven bqplot
jupyterlab ipywidgets ipyleaflet nbconvert quandl \  
&& jupyter serverextension enable \--py jupyterlab --sys-prefix \  
&& jupyter labextension install @jupyterlab/vega3-extension
@jupyterlab/geojson-extension @jupyterlab/plotly-extension
@jupyterlab/vega3-extension jupyterlab_bokeh bqplot  
  
# Prolog & bash Kernel  
RUN pip install calysto_prolog bash_kernel \  
&& python3 -m calysto_prolog install \  
&& python3 -m bash_kernel.install  
  
# Scala Kernel  
WORKDIR /usr/local/bin  
RUN curl -L -o coursier https://git.io/vgvpD && chmod +x coursier  
WORKDIR /opt/  
RUN git clone https://github.com/jupyter-scala/jupyter-scala.git  
WORKDIR /opt/jupyter-scala  
RUN ./jupyter-scala --id scala1 --name "Jupyter Scala" \--global  
  
# jupyterlab_voyager  
WORKDIR /opt  
RUN npm install --global yarn && git clone https://github.com/altair-
viz/jupyterlab_voyager.git  
COPY package.json /opt/jupyterlab_voyager/  
WORKDIR /opt/jupyterlab_voyager  
RUN yarn install && jupyter labextension link .  
  
# ijavascript  
RUN npm install --unsafe-perm --save-prod --verbose -g
https://github.com/n-riesco/ijavascript.git && ijsinstall  
  
# beakerx  
RUN conda install -y beakerx=0.10.0  
  
# Working directory  
WORKDIR /notebooks  
VOLUME /notebooks  
  
EXPOSE 8007  
CMD ["/root/miniconda3/bin/python", "/root/miniconda3/bin/jupyter", "lab", "--
no-browser", "--allow-root", "--port=8007", "--ip=0.0.0.0" ]  

