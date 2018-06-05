FROM gcc:4.9  
WORKDIR /root/install  
  
RUN useradd -ms /bin/bash nanograv  
  
# install cmake  
RUN apt-get -y update && \  
apt-get -y install cmake && \  
apt-get clean  
  
# install a few other basic tools  
RUN apt-get -y install less gawk vim && \  
apt-get clean  
  
# make calceph  
RUN wget -q
https://www.imcce.fr/content/medias/recherche/equipes/asd/calceph/calceph-2.3.2.tar.gz
&& \  
tar zxvf calceph-2.3.2.tar.gz && \  
cd calceph-2.3.2 && \  
./configure --prefix=/usr/local && \  
make && make install && \  
cd .. && rm -rf calceph-2.3.2 calceph-2.3.2.tar.gz  
  
WORKDIR /home/nanograv  
  
# copy in NANOGrav 11yr data  
# (data is owned by root and cannot be modified!)  
RUN mkdir -p nano11y_data/partim nano11y_data/noisefiles  
COPY nano11y_data/partim/* nano11y_data/partim/  
COPY nano11y_data/noisefiles/* nano11y_data/noisefiles/  
  
# copy in analysis code  
RUN mkdir models/  
COPY models/* models/  
COPY utils.py psrlist.txt /home/nanograv/  
RUN chown nanograv:nanograv models/* utils.py  
  
# analysis notebook  
COPY analysis.ipynb /home/nanograv/  
RUN chown nanograv:nanograv analysis.ipynb  
  
USER nanograv  
RUN mkdir /home/nanograv/.local  
  
ENV LD_LIBRARY_PATH="/usr/local/lib"  
# make tempo2  
RUN git clone https://bitbucket.org/psrsoft/tempo2 && \  
cd tempo2 && \  
./bootstrap && \  
./configure --prefix=/home/nanograv/.local \--with-calceph=/usr/local && \  
make && make install && \  
mkdir -p /home/nanograv/.local/share/tempo2 && \  
cp -Rp T2runtime/* /home/nanograv/.local/share/tempo2/. && \  
cd .. && rm -rf tempo2  
  
ENV TEMPO2=/home/nanograv/.local/share/tempo2  
  
# get extra ephemeris  
RUN cd /home/nanograv/.local/share/tempo2/ephemeris && \  
wget -q ftp://ssd.jpl.nasa.gov/pub/eph/planets/bsp/de435t.bsp && \  
wget -q ftp://ssd.jpl.nasa.gov/pub/eph/planets/bsp/de436t.bsp && \  
wget -q https://github.com/nanograv/tempo/raw/master/ephem/DE435.1950.2050 &&
\  
wget -q https://github.com/nanograv/tempo/raw/master/ephem/DE436.1950.2050  
  
# install miniconda  
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh && \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /home/nanograv/.local/miniconda
&& \  
rm Miniconda3-latest-Linux-x86_64.sh  
  
ENV
PATH="/home/nanograv/.local/miniconda/bin:/home/nanograv/.local/bin:${PATH}"  
# install basic Python packages  
RUN conda install -y numpy cython scipy && \  
conda clean -a  
  
# install libstempo (before other Anaconda packages, esp. matplotlib, so
there's no libgcc confusion)  
# get 2.3.3, specifically at 25 Aug 2017 (git sha 9cb7552)  
RUN pip install --install-option="--with-tempo2=/home/nanograv/.local"
git+https://github.com/vallis/libstempo@9cb7552  
  
# install more Python packages  
RUN conda install -y matplotlib ipython jupyter notebook h5py mpi4py numexpr
statsmodels astropy ephem runipy && \  
conda clean -a  
  
ENV MKL_NUM_THREADS=4  
# Jupyter notebook extensions  
RUN pip install jupyter_contrib_nbextensions && \  
jupyter contrib nbextension install --user  
  
# non-standard-Anaconda packages  
RUN pip install healpy line_profiler jplephem corner numdifftools  
  
# manually build SuiteSparse against Intel MKL  
USER root  
RUN wget -q
http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-5.1.0.tar.gz && \  
tar -xzf SuiteSparse-5.1.0.tar.gz && \  
cd SuiteSparse && \  
make install INSTALL=/usr/local \  
BLAS="-L/home/nanograv/.local/miniconda/lib -lmkl_rt" \  
LAPACK="-L/home/nanograv/.local/miniconda/lib -lmkl_rt" && \  
cd .. && rm -rf SuiteSparse/ SuiteSparse-5.1.0.tar.gz  
USER nanograv  
# install scikit-sparse  
RUN pip install --global-option=build_ext --global-option="-L/usr/local/lib"
scikit-sparse  
  
# install PTMCMCSampler (and py3 compatible acor)  
RUN pip install git+https://github.com/dfm/acor.git@master  
RUN pip install git+https://github.com/jellis18/PTMCMCSampler@master  
  
# install enterprise (v1.0.0)  
RUN pip install git+https://github.com/nanograv/enterprise@v1.0.0  
  
# matplotlib rc (default backend: Agg)  
RUN mkdir -p /home/nanograv/.config/matplotlib  
COPY matplotlibrc /home/nanograv/.config/matplotlib  
  
# default entry command:  
CMD jupyter notebook --no-browser --port 8888 --ip=0.0.0.0  

