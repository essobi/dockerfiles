FROM jupyter/scipy-notebook  
  
USER root  
  
RUN apt-get update -q && \  
apt-get install -qy \  
texlive-xetex \  
imagemagick \  
wkhtmltopdf \  
curl  
  
RUN jupyter-nbextension install
https://bitbucket.org/ipre/calico/downloads/calico-spell-check-1.0.zip  
  
USER $NB_USER  
  
RUN conda install --quiet --yes \  
-c jacksongs -c damianavila82 -c anaconda -c auto -c conda-forge \  
mpld3=0.3 \  
graphviz=2.38.0 \  
tensorflow \  
rise && \  
conda clean -tipsy  
  
RUN pip install --upgrade pdfkit  
  
RUN pip install \  
graphviz==0.4.10 \  
git+git://github.com/robjstan/tikzmagic.git \  
hide_code \  
python-crfsuite  
  
RUN jupyter nbextension install rise --py --sys-prefix && \  
jupyter nbextension install hide_code --py --sys-prefix && \  
jupyter nbextension install --user
https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/toc.js && \  
curl -L
https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/toc.css >
$(jupyter --data-dir)/nbextensions/toc.css  
  
RUN jupyter nbextension enable rise --py --sys-prefix && \  
jupyter nbextension enable calico-spell-check --sys-prefix && \  
jupyter nbextension enable hide_code --py --sys-prefix && \  
jupyter serverextension enable hide_code --py --sys-prefix && \  
jupyter nbextension enable toc  
  
WORKDIR /home/zju/work  

