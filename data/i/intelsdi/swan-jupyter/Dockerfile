FROM jupyter/minimal-notebook:df7a34bebed0  
  
RUN conda install -q -y nomkl cassandra-driver pandas pep8 pylint \  
&& conda clean -y -a -v  
RUN pip install pivottablejs  
  
COPY test_data/ $HOME/test_data  
COPY example.ipynb *.py $HOME/  
COPY NOTICE $HOME/  
  
# Switch to root and fix permissions.  
USER root  
RUN chown -v -R $NB_USER:users /home/$NB_USER  
# Switch back to jovyan user.  
USER $NB_USER  

