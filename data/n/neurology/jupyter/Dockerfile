FROM python:3.6.0  
COPY start.sh /start.sh  
VOLUME /notebooks  
WORKDIR /notebooks  
EXPOSE 8888  
CMD ["/start.sh"]  
  
RUN apt-get update && apt-get install -y r-recommended  
RUN pip3 --no-cache-dir install numpy pandas  
RUN pip3 --no-cache-dir install seaborn jupyter numexpr nibabel scikit-learn
scikit-image python-slugify openpyxl xlrd  
RUN pip3 --no-cache-dir install nilearn  
RUN pip3 --no-cache-dir install elasticsearch certifi  
RUN pip3 --no-cache-dir install statsmodels  
RUN pip3 --no-cache-dir install requests  

