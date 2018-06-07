# Usage:  
# docker build -t andaag/large_notebook3 .  
FROM andaag/sklearn_notebook3  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.utf-8  
RUN mkdir /root/.ssh /nltk_data && ln -s /nltk_data /usr/share/nltk_data  
RUN ssh-keyscan -t rsa github.com > /root/.ssh/known_hosts  
  
RUN apt-get install -y sudo && apt-get clean -y  
RUN conda install -y nltk seaborn gensim ipywidgets boto  
RUN pip install ggplot  
RUN pip install git+https://github.com/andaag/scikit_helpers  
RUN apt-get update && apt-get -y install build-essential && pip install
xgboost==0.4a29 && apt-get remove -y build-essential && apt-get -y autoremove
&& apt-get clean -y  
RUN conda upgrade --all -y  
#latest was broken..  
RUN conda install numpy==1.10.4 -y  
  
RUN groupadd ml && useradd ml -m -g ml -u 1000  
ADD start.sh /home/ml/  
  
RUN sudo -s -H -u ml -- env PATH="/opt/miniconda/bin:$PATH" jupyter notebook
--generate-config  
RUN sed -i \  
-e "s/^# c.NotebookApp.ip = 'localhost'$/c.NotebookApp.ip = '0.0.0.0'/" \  
-e "s/^# c.NotebookApp.port = 8888$/c.NotebookApp.port = 8888/" \  
-e "s;^# c.NotebookApp.notebook_dir = '/.*'$;c.NotebookApp.notebook_dir = '/ml';" \  
-e "s/^# c.NotebookApp.open_browser = True$/c.NotebookApp.open_browser = False/" \  
-e "s/^# c.IPKernelApp.extensions = \\[\\]$/c.IPKernelApp.extensions = ['']/" \  
/home/ml/.jupyter/jupyter_notebook_config.py  
  
RUN mkdir -p /home/ml/.config/matplotlib/ /root/.config/matplotlib  
RUN echo "backend : agg" > /home/ml/.config/matplotlib/matplotlibrc  
RUN echo "backend : agg" > /root/.config/matplotlib/matplotlibrc  
RUN chown ml:ml -R /home/ml/  
  
VOLUME /ml  
VOLUME /nltk_data  
WORKDIR /ml  
  
EXPOSE 8888  
CMD chown ml:ml /ml /nltk_data && sudo -s -E -H -u ml -- env
PATH="/opt/miniconda/bin:$PATH" bash /home/ml/start.sh  
  

