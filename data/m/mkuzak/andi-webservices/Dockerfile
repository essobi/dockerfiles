FROM rocker/r-base  
  
RUN apt-get update  
RUN apt-get install -y python python-pip python-dev  
RUN pip install rpy2  
RUN Rscript -e 'install.packages("jsonlite",
repos="https://cran.rstudio.com")'  
  
ADD $PWD /app  
  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
EXPOSE 5000  
CMD python hello.py  

