FROM jupyter/scipy-notebook:4ebeb1f2d154  
  
MAINTAINER Ben Rowland "browland@partners.org"  
USER root  
  
RUN apt-get update \  
&& apt-get install -y neurodebian-archive-keyring  
  
# install fsl  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install fsl-5.0-core \  
# Run configuration script for normal usage  
&& echo ". /etc/fsl/5.0/fsl.sh" >> /home/jovyan/.bashrc  
  
# Configure environment  
ENV FSLDIR=/usr/share/fsl/5.0/  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
ENV PATH=$PATH:/usr/lib/fsl/5.0  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/fsl/5.0  
# install niftyreg  
RUN apt-get update \  
&& apt-get -y install cmake  
  
RUN mkdir /opt/niftyreg-src && \  
mkdir /opt/niftyreg-build && \  
git clone https://cmiclab.cs.ucl.ac.uk/mmodat/niftyreg.git /opt/niftyreg-src  
  
WORKDIR /opt/niftyreg-build  
  
RUN PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin && \  
cmake -D CMAKE_BUILD_TYPE=Release /opt/niftyreg-src && \  
make && \  
make install && \  
PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/fsl/5.0  
  
# install dev version of nipype to include niftyreg  
#RUN git clone https://github.com/nipy/nipype.git /opt/nipype  
# install tarquin  
RUN wget --quiet
https://sourceforge.net/projects/tarquin/files/TARQUIN_4.3.10/TARQUIN_Linux_4.3.10.tar.gz/download
-O /tmp/tarquin.tar.gz && \  
mkdir /etc/tarquin && \  
tar -zxvf /tmp/tarquin.tar.gz -C /etc/tarquin --strip-components=1  
  
ENV PATH /etc/tarquin:$PATH  
  
RUN apt-get install -y libxml2-dev libxslt1-dev  
  
# copy the examples directory in to the notebook root and change the owner  
COPY ./examples /home/$NB_USER/work/examples/  
RUN chown $NB_USER -R /home/$NB_USER/work/examples/  
  
USER $NB_USER  
WORKDIR /home/jovyan/work  
  
#RUN pip install nibabel traits nose future simplejson lxml prov pbr mock
xvfbwrapper  
RUN conda update -n base conda && \  
pip install --upgrade pip && \  
pip install pyx nipype pydicom  
  
#RUN pip install https://github.com/nipy/nipype/archive/master.zip  
#RUN pip install /opt/nipype  
#RUN pip install https://github.com/darcymason/pydicom/archive/master.zip  
RUN git clone https://github.com/openmrslab/suspect.git /home/jovyan/suspect
&& \  
pip install suspect==0.3.8  
  
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 ipython
ipykernel kernda && \  
conda clean -tipsy  
  
USER root  
  
# Create a global kernelspec in the image and modify it so that it properly
activates  
# the python2 conda environment.  
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install && \  
$CONDA_DIR/envs/python2/bin/kernda -o -y
/usr/local/share/jupyter/kernels/python2/kernel.json  
  
USER $NB_USER  
RUN /bin/bash -c "source activate python2 && pip install pygamma"  
  

