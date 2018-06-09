FROM r-base  
  
COPY install.R /usr/local/src/myscripts/install.R  
WORKDIR /usr/local/src/myscripts  
RUN Rscript install.R  
  
COPY . /usr/local/src/myscripts  
  
CMD ["Rscript", "loadData.r"]  

