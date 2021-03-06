FROM docker.io/pmgbergen/porepylib:base  
MAINTAINER dbaroli <davide.baroli@uni.lu>  
  
USER root  
  
ENTRYPOINT ["sudo","/sbin/my_init","--
quiet","--","sudo","-u","porepy","/bin/bash","-l","-c"]  
CMD ["/bin/bash","-i"]  
  
  
  
RUN apt-get -qq update && \  
apt-get -y --with-new-pkgs \  
-o Dpkg::Options::="--force-confold" upgrade && \  
apt-get -y install curl && \  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get update -y; apt-get install -y --force-yes --fix-missing --no-install-
recommends curl git git-lfs unzip tree subversion vim cmake bison g++ gfortran
openmpi-bin pkg-config wget \  
libpcre3-dev bison flex swig libglu1-mesa libxcursor-dev libxft-dev
libxinerama-dev libmed1v5 libpng12-0 liboce-foundation10 liboce-modeling10
pyqt5-dev-tools bash-completion libxt6 &&\  
git lfs install && \  
apt-get clean && \  
#linking  
ln -s /usr/lib/x86_64-linux-gnu/libGLU.so.1 /usr/lib/libGLU.so.1 &&\  
ln -s /usr/lib/x86_64-linux-gnu/libSM.so.6 /usr/lib/libSM.so.6 && \  
ln -s /usr/lib/x86_64-linux-gnu/libICE.so.6 /usr/lib/libICE.so.6 && \  
ln -s /usr/lib/x86_64-linux-gnu/libX11.so.6 /usr/lib/libX11.so.6 && \  
ln -s /usr/lib/x86_64-linux-gnu/libXext.so.6 /usr/lib/libXext.so.6 && \  
ln -s /usr/lib/x86_64-linux-gnu/libXt.so.6 /usr/lib/libXt.so.6 && \  
ln -s /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1 /usr/lib/libGL.so.1 &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /tmp  
  
ENV GMSH_VERSION 2.11.0  
RUN wget http://gmsh.info/bin/Linux/gmsh-${GMSH_VERSION}-Linux64.tgz &&\  
tar xf gmsh-${GMSH_VERSION}-Linux64.tgz && \  
cp gmsh-${GMSH_VERSION}-Linux/bin/gmsh /usr/local/bin/gmsh && \  
rm -rf /tmp/*  
  
RUN cd /tmp && \  
wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O
conda.sh && \  
chmod +x conda.sh && \  
bash conda.sh -b -p /home/porepy/.conda && \  
rm /tmp/*  
  
RUN id porepy &&\  
chown -R porepy:porepy /home  
  
  
USER porepy  
  
ENV PATH=/home/porepy/.conda/bin:$PATH  
  
  
RUN echo "PATH=/home/porepy/.conda/bin:$PATH" >> ~/.profile && \  
/bin/bash -c -l 'source ~/.profile'  
  
RUN hash -r && \  
conda config --set always_yes yes --set changeps1 no && \  
conda update -q conda && \  
conda info -a && \  
conda create --yes -n porepy python="3.6"  
RUN /bin/bash -c -l 'source activate porepy'  
  
ENV PATH /home/porepy/.conda/envs/porepy/bin:$PATH  
ENV CONDA_DEFAULT_ENV porepy  
ENV CONDA_PREFIX /home/porepy/.conda/envs/porepy  
  
  
RUN conda install --yes numpy scipy matplotlib pip nose sip llvmlite numba &&\  
conda install -c https://conda.anaconda.org/clinicalgraphics vtk &&\  
pip install setuptools && \  
pip install numpy-stl && \  
pip install coveralls && \  
pip install coverage &&\  
pip install cython &&\  
pip install jupyter ipython pdbpp  
  
  
WORKDIR $POREPY_HOME  
RUN mkdir -p $POREPY_HOME/.config/matplotlib  
COPY matplotlibsrc $POROPY_HOME/.config/matplotlib/matplotlibrc  
  
  
COPY dependencies $POROPY_HOME/.dependencies  
RUN pip install --no-cache-dir -r $POROPY_HOME/.dependencies  
RUN /bin/bash -c -l 'echo "source activate porepy">>~/.profile' && \  
/bin/bash -c -l 'echo
"PYTHONPATH=/home/porepy/conda/envs/porepy/lib/python3.6/site-
packages:$PYTHONPATH">>~/.profile'  
  
COPY install $POREPY_HOME  
RUN sudo chmod +x install  
  
  
  
  

