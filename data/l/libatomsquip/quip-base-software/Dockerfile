# Software applications  
# Split from base image to keep under the 2 hr build  
# limit on docker hub.  
# Base QUIP image has build dependencies  
FROM libatomsquip/quip-base  
  
MAINTAINER Tom Daff "tdd20@cam.ac.uk"  
##############  
## Python 3 ##  
##############  
# Put Python 3 packages in a virtualenv  
# include `py3` command as a quick alias  
# to activate  
ENV PY3_PATH /opt/python3/  
  
RUN virtualenv -p python3 ${PY3_PATH}  
RUN echo "alias py3='source ${PY3_PATH}/bin/activate'" >> /etc/bash.bashrc  
  
ENV PYTHON3 ${PY3_PATH}/bin/python  
ENV PIP3 ${PY3_PATH}/bin/pip  
  
RUN ${PIP3} install --upgrade pip  
RUN ${PIP3} install --no-cache-dir jupyter numpy scipy matplotlib ase pyamg \  
imolecule sphinx spglib nglview  
# Requires numpy to install  
RUN ${PIP3} install --no-cache-dir gpaw  
  
RUN ${PIP3} install git+https://github.com/libAtoms/matscipy.git  
  
RUN ${PIP3} install --global-option=build_ext --global-
option="-L/opt/OpenBLAS/lib" atomistica  
  
RUN ${PY3_PATH}/bin/jupyter nbextension enable \--py --sys-prefix
widgetsnbextension  
RUN ${PY3_PATH}/bin/jupyter nbextension enable \--py --sys-prefix nglview  
  
# Add kernel to main Jupyter  
# POSIX echo does not take -e already works with newlines  
RUN ln -s ${PY3_PATH}/share/jupyter/kernels/python3
/usr/local/share/jupyter/kernels/ \  
&& echo '{\n "argv": [\n "'${PYTHON3}'",\n "-m",\n "ipykernel_launcher",\n
"-f",\n "{connection_file}"\n ],\n "display_name": "Python 3",\n "language":
"python"\n}' > /usr/local/share/jupyter/kernels/python3/kernel.json  
  
# AmberTools (no Amber)  
ENV AMBERHOME /opt/amber16/  
  
# Never write the tests to disk (1GB) and remove src (500MB) after compilation  
RUN mkdir -p ${AMBERHOME} \  
&& cd ${AMBERHOME} \  
&& curl "http://ambermd.org/cgi-
bin/AmberTools17-get.pl?Name=quipbot&Institution=NA&City=NA&State=NA&Country=NA&OS=linux-64"
\  
| tar xj --exclude='*/test/*' \--strip-components 1 \  
&& ./update_amber --show-applied-patches \  
&& ./update_amber --update \  
&& ./update_amber --show-applied-patches \  
&& ./configure --with-python `which python` --python-install global -noX11 gnu
\  
&& make install \  
&& ./configure --with-python `which python` --python-install global -noX11
-mpi gnu \  
&& make install \  
&& rm -rf ${AMBERHOME}/test ${AMBERHOME}/AmberTools  
  
ENV PATH ${AMBERHOME}/bin:${PATH}  
  
  

