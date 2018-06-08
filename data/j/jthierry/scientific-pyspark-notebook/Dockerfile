FROM jthierry/minimal-pyspark-notebook  
  
USER root  
  
# libav-tools for matplotlib anim  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libav-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
# Install Python 3 packages  
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to  
# use notebook-friendly backends in these images  
RUN conda install --yes \  
'ipywidgets=5.1*' \  
'pandas=0.18*' \  
'numexpr=2.5*' \  
'matplotlib=1.5*' \  
'scipy=0.18*' \  
'seaborn=0.7*' \  
'scikit-learn=0.17*' \  
'scikit-image=0.11*' \  
'sympy=1.0*' \  
'cython=0.23*' \  
'patsy=0.4*' \  
'statsmodels=0.6*' \  
'cloudpickle=0.1*' \  
'dill=0.2*' \  
'numba=0.23*' \  
'bokeh=0.12*' \  
'sqlalchemy=1.0*' \  
'hdf5=1.8.17' \  
'h5py=2.6*' \  
'tensorflow=0.9*' \  
'nltk=3.2*' \  
'beautifulsoup4=4.5*' && \  
conda remove --yes \--force qt pyqt && \  
conda clean -tipsy  
  
# Useful from kaggle/python  
RUN pip install --upgrade mpld3 && \  
pip install mplleaflet && \  
pip install gpxpy && \  
pip install arrow && \  
pip install sexmachine && \  
pip install Geohash && \  
pip install deap && \  
pip install tpot && \  
pip install haversine && \  
pip install toolz cytoolz && \  
pip install sacred && \  
pip install plotly && \  
pip install git+https://github.com/nicta/dora.git && \  
pip install git+https://github.com/hyperopt/hyperopt.git && \  
# tflearn. Deep learning library featuring a higher-level API for TensorFlow.
http://tflearn.org  
pip install git+https://github.com/tflearn/tflearn.git && \  
pip install fitter && \  
pip install langid && \  
# Delorean. Useful for dealing with datetime  
pip install delorean && \  
pip install trueskill && \  
pip install heamy && \  
# Useful data exploration libraries (for missing data and generating reports)  
pip install missingno && \  
pip install pandas-profiling && \  
pip install s2sphere && \  
# clean up pip cache  
rm -rf $NB_USER/.cache/pip/*  
  
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix  
RUN mkdir -p $HOME/.ipython/profile_default/startup  
COPY mplimporthook.py $HOME/.ipython/profile_default/startup/  

