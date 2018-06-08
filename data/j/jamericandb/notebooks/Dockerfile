FROM jupyter/datascience-notebook  
  
# Install Dato's GraphLab  
# ENV GRAPHLAB_EMAIL j.american.db@gmail.com  
# ARG GRAPHLAB_LICENSE  
# ARG GRAPHLAB_VERSION=1.9  
# RUN $PIP2 install --upgrade \  
# https://get.dato.com/GraphLab-
Create/$GRAPHLAB_VERSION/$GRAPHLAB_EMAIL/$GRAPHLAB_LICENSE/GraphLab-Create-
License.tar.gz  
# Install GPU-acclerated graphlab  
# RUN $PIP2 install --upgrade \  
# http://static.dato.com/files/graphlab-create-gpu/graphlab-
create-$GRAPHLAB_VERSION.gpu.tar.gz  
# Install mlsl  
#COPY mlsl /home/jovyan/mlsl  
#RUN pip install -e /home/jovyan/mlsl['test']  
## Not sure how well it behaves in Python2, guess we'll find out!  
#RUN pip2 install -e /home/jovyan/mlsl['test']  
# Python2  
# TODO Remove once IPython version >=4.2.1  
# http://stackoverflow.com/questions/37232446/ipython-console-cant-locate-
backports-shutil-get-terminal-size-and-wont-load  
RUN pip2 install -U pip && \  
pip2 install -I backports.shutil_get_terminal_size  
RUN conda install -n python2 --yes \  
pymc  
  
# Python3  
RUN conda install --yes \  
"beautifulsoup4>=4.4.1" \  
joblib \  
"mpld3" \  
"sphinx" \  
"pytables"  
RUN pip install -U pip && \  
pip install -U \  
aiohttp \  
google-api-python-client  
  
# Copy in custom javascript modifications to the notebook  
COPY custom.js /home/jovyan/.jupyter/custom.js  
WORKDIR /home/jovyan/work  

