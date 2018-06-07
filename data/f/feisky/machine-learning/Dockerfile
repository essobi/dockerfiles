FROM tensorflow/tensorflow  
MAINTAINER feisky <feiskyer@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential git && \  
pip install seaborn python-dateutil dask pytagcloud pyyaml ggplot joblib vega
&& \  
jupyter nbextension install --user --py vega && \  
jupyter nbextension enable vega --user --py && \  
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
# tflean. Deep learning library featuring a higher-level API for TensorFlow.
http://tflearn.org  
pip install git+https://github.com/tflearn/tflearn.git && \  
pip install fitter && \  
pip install langid && \  
# Delorean. Useful for dealing with datetime  
pip install delorean && \  
pip install trueskill && \  
pip install heamy && \  
pip install vida && \  
# Useful data exploration libraries (for missing data and generating reports)  
pip install missingno && \  
pip install pandas-profiling && \  
pip install s2sphere && \  
pip install git+https://github.com/fmfn/BayesianOptimization.git && \  
pip install matplotlib-venn && \  
pip install pyldavis && \  
pip install git+git://github.com/rasbt/mlxtend.git#egg=mlxtend && \  
pip install altair && \  
# clean up pip cache  
rm -rf /root/.cache/pip/* && \  
apt-get clean  
  
ENV GOPATH /go  
ENV PATH
/go/bin:/usr/local/bin:/usr/local/go/bin/:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN curl -sL https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz
| tar -C /usr/local -zxf - && \  
go get golang.org/x/tools/cmd/goimports && \  
go get -tags zmq_3_x github.com/gopherds/gophernotes && \  
mkdir -p ~/.ipython/kernels/gophernotes && \  
cp -r $GOPATH/src/github.com/gopherds/gophernotes/kernel/*
~/.ipython/kernels/gophernotes  

