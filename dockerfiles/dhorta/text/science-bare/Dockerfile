FROM ubuntu

RUN apt-get update -q
RUN apt-get install -y -q build-essential libc6 gfortran g++ \
    python python-setuptools cython python-numpy python-scipy \
    python-matplotlib pkg-config libfreetype6-dev libpng12-dev \
    libhdf5-dev liblapack-dev
RUN apt-get install python-pip -qq -y
RUN pip install h5py -q
RUN apt-get install git -qq -y
RUN apt-get install golang -qq -y
ENV GOPATH /home/gocode
ENV PATH /home/gocode/bin:$PATH
RUN pip install pandas -q
RUN pip install twine -q
RUN go get github.com/aktau/github-release
RUN apt-get install libffi-dev libssl-dev -qq -y
RUN pip install pyopenssl ndg-httpsclient pyasn1
RUN pip install cryptography
RUN pip install urllib3[secure]
RUN apt-get install -y -q swig
