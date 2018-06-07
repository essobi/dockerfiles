FROM continuumio/miniconda3:4.2.12  
LABEL version=0.7.3  
  
ADD ./extentdiffimages /opt/extentdiffimages/extentdiffimages  
ADD ./.flake8rc /opt/extentdiffimages  
ADD ./gunicorn_conf.py /opt/extentdiffimages  
ADD ./cmd.sh /opt/extentdiffimages  
ADD ./environment.yml /opt/extentdiffimages  
  
WORKDIR /opt/extentdiffimages  
  
RUN conda env update -f environment.yml -n root  
  
EXPOSE 5000  
CMD ["./cmd.sh"]  

