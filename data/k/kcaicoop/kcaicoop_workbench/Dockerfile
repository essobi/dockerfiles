FROM jupyter/base-notebook  
USER root  
RUN mkdir /installation  
RUN chown -R 1000:100 /installation  
RUN mkdir /data  
RUN chown -R 1000:100 /data  
RUN touch /data/PUT_DATA_HERE  
RUN mkdir /working  
RUN chown -R 1000:100 /working  
USER jovyan  
VOLUME ["/data"]  
VOLUME ["/working"]  
USER jovyan  
  
RUN pip install tensorflow  
RUN pip install sklearn  
RUN pip install statsmodels  
RUN pip install seaborn  
RUN pip install pandas  
RUN pip install numpy  
  
WORKDIR "/working"  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
USER jovyan  

