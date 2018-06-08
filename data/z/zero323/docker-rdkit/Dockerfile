# vim:set ft=dockerfile:  
FROM zero323/rdkit:base  
MAINTAINER Maciej Szymkiewicz <matthew.szymkiewicz@gmail.com>  
  
RUN conda install -y ipython-notebook  
  
EXPOSE 8888  
CMD jupyter notebook --ip=*  

