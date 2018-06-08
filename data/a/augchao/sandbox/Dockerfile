FROM jupyter/datascience-notebook  
  
MAINTAINER August F.Y. Chao <AugChao@itri.org.tw>  
  
RUN /opt/conda/bin/pip2 install numpy pandas scipy matplotlib scikit-learn
nltk seaborn cython seaborn cython gensim beautifulsoup4  
  
RUN /opt/conda/bin/conda install -n python2 -y -c anaconda pillow  
  
EXPOSE 8888  
WORKDIR /home/$NB_USER/work  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
COPY start.sh /usr/local/bin/  
RUN chmod a+x /usr/loca/bin/start.sh  
  
USER jovyan  

