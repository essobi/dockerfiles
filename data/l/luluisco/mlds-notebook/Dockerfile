FROM jupyter/all-spark-notebook  
  
ARG TEST_ONLY_BUILD  
  
USER root  
  
# Install all OS dependencies for openai gym  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
python-numpy \  
python-dev \  
cmake \  
zlib1g-dev \  
libjpeg-dev \  
xvfb \  
libav-tools \  
xorg-dev \  
python-opengl \  
libboost-all-dev \  
libsdl2-dev \  
swig \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install ffmpeg for video handling  
RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -yq --no-install-recommends ffmpeg  
  
# Switch back to jovyan to avoid accidental container running as root  
USER $NB_USER  
RUN conda update -n base conda  
  
# Add channels to conda to install custom packages  
RUN conda config --add channels menpo # for opencv  
  
# Set the working directory  
WORKDIR /home/$NB_USER/work  
  
# Install binary packages with conda from requirements-conda.txt.  
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to  
# use notebook-friendly backends in these images  
#ONBUILD COPY requirements-conda.txt /home/jovyan/work  
#ONBUILD RUN conda install --quiet --yes --file requirements-conda.txt && \  
#conda remove --quiet --yes --force qt pyqt && \  
#conda clean -tipsy  
# Install python packages with pip from requirements-pip.txt  
#ONBUILD COPY requirements-pip.txt /home/jovyan/work  
#ONBUILD RUN pip install --no-cache-dir -r requirements-pip.txt  
# Deploy application code  
#ONBUILD COPY . /home/$NB_USER/work  
# Install H2O pysparkling requirements  
RUN pip install requests && \  
pip install tabulate && \  
pip install six && \  
pip install future && \  
pip install colorama  
  
# Expose H2O Flow UI ports  
EXPOSE 54321  
EXPOSE 54322  
EXPOSE 55555  
USER root  
RUN \  
cd /home/$NB_USER \  
&& wget -q http://h2o-release.s3.amazonaws.com/h2o/rel-
wolpert/11/h2o-3.18.0.11.zip \  
&& unzip h2o-3.18.0.11.zip \  
&& cd h2o-3.18.0.11 \  
&& mkdir -p /usr/local/h2o_jar/ \  
&& cp h2o.jar /usr/local/h2o_jar/ \  
&& cd .. \  
&& rm -rf h2o-3.18.0.11*  
  
# The following command removes the H2O module for Python.  
RUN pip uninstall h2o || true && pip install
http://h2o-release.s3.amazonaws.com/h2o/rel-
wolpert/11/Python/h2o-3.18.0.11-py2.py3-none-any.whl  
  
#https://s3.amazonaws.com/h2o-release/sparkling-water/rel-2.3/5/sparkling-
water-2.3.5.zip  
# Install H2O sparkling water  
RUN \  
cd /home/$NB_USER && \  
wget https://s3.amazonaws.com/h2o-release/sparkling-water/rel-2.3/5/sparkling-
water-2.3.5.zip && \  
unzip sparkling-water-2.3.5.zip && \  
cd sparkling-water-2.3.5 && \  
cp -R bin/* /usr/local/bin && \  
cd .. && \  
rm -rf sparkling-water-2.3.5*  
  
# Add sparkling-water's /bin folder to path  
#ENV PATH="/home/$NB_USER/sparkling-water-2.3.5/bin:${PATH}"  
RUN pip install h2o_pysparkling_2.3  
  
# Switch back to jovyan to avoid container running accidentally as root  
#USER $NB_USER  
USER root  
  
# Julia dependencies  
# install Julia packages in /opt/julia instead of $HOME  
ENV JULIA_PKGDIR=/opt/julia  
ENV JULIA_VERSION=0.6.2  
RUN mkdir /opt/julia-${JULIA_VERSION} && \  
cd /tmp && \  
wget -q https://julialang-s3.julialang.org/bin/linux/x64/`echo
${JULIA_VERSION} | cut -d. -f 1,2`/julia-${JULIA_VERSION}-linux-x86_64.tar.gz
&& \  
echo "dc6ec0b13551ce78083a5849268b20684421d46a7ec46b17ec1fab88a5078580
*julia-${JULIA_VERSION}-linux-x86_64.tar.gz" | sha256sum -c - && \  
tar xzf julia-${JULIA_VERSION}-linux-x86_64.tar.gz -C
/opt/julia-${JULIA_VERSION} \--strip-components=1 && \  
rm /tmp/julia-${JULIA_VERSION}-linux-x86_64.tar.gz  
RUN ln -fs /opt/julia-*/bin/julia /usr/local/bin/julia  
  
# Show Julia where conda libraries are \  
RUN mkdir /etc/julia && \  
echo "push!(Libdl.DL_LOAD_PATH, \"$CONDA_DIR/lib\")" >> /etc/julia/juliarc.jl
&& \  
# Create JULIA_PKGDIR \  
mkdir $JULIA_PKGDIR && \  
chown $NB_USER $JULIA_PKGDIR && \  
fix-permissions $JULIA_PKGDIR  
  
USER $NB_UID  
  
# R packages  
# R packages including IRKernel which gets installed globally.  
RUN conda install --quiet --yes \  
'rpy2=2.8*' \  
'r-base=3.4.1' \  
'r-irkernel=0.8*' \  
'r-plyr=1.8*' \  
'r-devtools=1.13*' \  
'r-tidyverse=1.1*' \  
'r-shiny=1.0*' \  
'r-rmarkdown=1.8*' \  
'r-forecast=8.2*' \  
'r-rsqlite=2.0*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-crayon=1.3*' \  
'r-randomforest=4.6*' \  
'r-htmltools=0.3*' \  
'r-sparklyr=0.7*' \  
'r-htmlwidgets=1.0*' \  
'r-hexbin=1.27*' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
# Add Julia packages. Only add HDF5 if this is not a test-only build since  
# it takes roughly half the entire build time of all of the images on Travis  
# to add this one package and often causes Travis to timeout.  
#  
# Install IJulia as jovyan and then move the kernelspec out  
# to the system share location. Avoids problems with runtime UID change not  
# taking effect properly on the .local folder in the jovyan home dir.  
USER root  
RUN apt-get install -y hdf5-tools  
USER $NB_UID  
  
RUN julia -e 'Pkg.init()' && \  
julia -e 'Pkg.update()' && \  
(test $TEST_ONLY_BUILD || julia -e 'Pkg.add("HDF5")') && \  
julia -e 'Pkg.add("Gadfly")' && \  
julia -e 'Pkg.add("PyCall")' && \  
julia -e 'Pkg.add("RCall")' && \  
julia -e 'Pkg.add("CxxWrap.jl")' && \  
julia -e 'Pkg.add("JavaCall.jl")' && \  
julia -e 'Pkg.add("RDatasets")' && \  
julia -e 'Pkg.add("IJulia")' && \  
# Precompile Julia packages \  
julia -e 'using IJulia' && \  
# move kernelspec out of home \  
mv $HOME/.local/share/jupyter/kernels/julia* $CONDA_DIR/share/jupyter/kernels/
&& \  
chmod -R go+rx $CONDA_DIR/share/jupyter && \  
rm -rf $HOME/.local && \  
fix-permissions $JULIA_PKGDIR $CONDA_DIR/share/jupyter  
  
# Install Tensorflow  
RUN conda install --quiet --yes \  
'tensorflow=1.5*' \  
'keras=2.1*' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
USER root  
# INSTALL THEANOS  
RUN apt-get update && apt-get install -y \  
build-essential \  
gfortran \  
git \  
wget \  
liblapack-dev \  
libopenblas-dev \  
python-dev \  
python-pip \  
python-nose \  
python-numpy \  
python-scipy \  
vim  
  
# Install bleeding-edge Theano  
RUN pip install --upgrade pip && \  
pip install --upgrade six && \  
pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
  
# Install gcc xgboost  
RUN pip install xgboost  
  
USER root  
RUN pip install py4j==0.10.6 psutil  
RUN pip install sos  
RUN pip install sos-notebook  
RUN python -m sos_notebook.install  
RUN pip install bash_kernel  
RUN python -m bash_kernel.install  
  
RUN pip install markdown-kernel  
#USER root  
USER $NB_UID  
#python custom  
ENV CUSTOM_DIR="$HOME/.custom"  
# VOLUME $CUSTOM_DIR  
RUN mkdir $CUSTOM_DIR  
#ENV PIPI=$PIP_TARGET  
ENV PIPO_TARGET=$CUSTOM_DIR/python  
RUN mkdir $PIPO_TARGET  
ENV PYTHONUSERBASE=$PIPO_TARGET  
ENV PYTHONPATH=$PIPO_TARGET:$PYTHONPATH  
  
#r custom  
RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com"))'
>/home/$NB_USER/.Rprofile  
RUN mkdir $CUSTOM_DIR/R  
ENV R_LIBS_USER=$CUSTOM_DIR/R:$R_LIBS_USER  
  
#julia custom  
RUN mkdir -p $CUSTOM_DIR/julia  
#RUN ln -s $CUSTOM_DIR/julia/v0.6/REQUIRE $JULIA_PKGDIR/v0.6  
ENV JULIA_LOAD_PATH=$JULIA_PKGDIR/v0.6  
ENV JULIA_PKGDIR=$CUSTOM_DIR/julia  
  
RUN julia -e 'Pkg.init()'  
  
#ENV NB_USER=mlds  
ENV NB_USER_CUSTOM=mlds  
USER root  
#RUN start.sh true  
RUN echo $NB_USER:$NB_USER_CUSTOM | chpasswd  
RUN usermod -a -G sudo $NB_USER  
RUN ln -s /home/$NB_USER /home/$NB_USER_CUSTOM  
  
COPY $NB_USER_CUSTOM.sh /usr/local/bin  
RUN chmod o+x /usr/local/bin/$NB_USER_CUSTOM.sh  
RUN conda install -c conda-forge jupyter_nbextensions_configurator  
RUN cp /etc/sudoers /root/sudoers.bak  
RUN echo "$NB_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN echo 'alias _sudo="/usr/bin/sudo"' >> /home/$NB_USER/.bashrc  
RUN echo 'alias sudo="sudo PATH=\$PATH"' >> /home/$NB_USER/.bashrc  
USER $NB_UID  

