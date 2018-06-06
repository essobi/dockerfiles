FROM underworldcode/underworld2:2.5.1b_magnus  
MAINTAINER d.sandiford@unimelb.edu  
  
# Dan dependencies  
WORKDIR /opt  
  
RUN pip install networkx  
RUN pip install easydict  
RUN pip install naturalsort  
RUN pip install "networkx==1.11"  
RUN pip install pint  
RUN pip install pandas  
  
ENV UW2_DIR /opt/underworld2  
  
RUN cd /opt && \  
rm -fr underworld2 && \  
git clone \--branch "slade" https://github.com/underworldcode/underworld2  
  
RUN cd underworld2/libUnderworld && \  
./configure.py --with-debugging=0 --petsc-dir=/opt/petsc --hdf5-dir=/opt/petsc
&& \  
./compile.py  
  
# copy this file over so that no password is required  
#COPY jupyter_notebook_config.json
/home/root/.jupyter/jupyter_notebook_config.json  
RUN git clone https://github.com/dansand/UWsubduction.git  
  
# change user and update pythonpath  
ENV PYTHONPATH $PYTHONPATH:$UW2_DIR  
#ENV PYTHONPATH /workspace/user_data/UWGeodynamics:$PYTHONPATH  
ENV PYTHONPATH /opt/UWsubduction:$PYTHONPATH  
  
# move back to workspace directory  
WORKDIR /workspace  
  
# launch notebook  
CMD ["jupyter", "notebook", "--ip='*'", "--no-browser"]  

