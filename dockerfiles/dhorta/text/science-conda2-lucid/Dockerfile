FROM ubuntu:lucid

RUN apt-get update
RUN apt-get install --yes wget build-essential

RUN wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh \
         -O miniconda.sh -nv
RUN chmod +x miniconda.sh
RUN ./miniconda.sh -b
ENV PATH /miniconda2/bin:$PATH

RUN conda install -y -q numpy cython scipy numba conda-build \
                        setuptools matplotlib h5py pandas \
                        scikit-learn
RUN conda install -y -q anaconda-client
RUN conda config --add channels r
RUN conda install r rpy2

RUN conda install -y -q pip
RUN pip install twine -q
RUN conda install -y -q scikit-learn
RUN apt-get install -y -q python-software-properties
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get update -q
RUN apt-get install git -qq -y

RUN cd $HOME && wget \
    https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz \
    --no-check-certificate
RUN cd $HOME && tar xzf go1.6.linux-amd64.tar.gz
ENV GOROOT $HOME/go
ENV PATH $PATH:$GOROOT/bin
RUN mkdir /home/gocode
ENV GOPATH /home/gocode

RUN go get github.com/aktau/github-release
RUN apt-get install libffi-dev libssl-dev -qq -y
RUN pip install pyopenssl ndg-httpsclient pyasn1
RUN pip install urllib3[secure]
RUN conda install -y -q swig
