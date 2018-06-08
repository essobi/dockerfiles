FROM v4tech/prod-python:latest  
MAINTAINER Stewart V. Wright <stewart@vifortech.com>  
  
# These commands run when a new image is built  
ONBUILD ADD .condarc /root/.condarc  
ONBUILD ADD environment.yml /environment.yml  
ONBUILD RUN conda env create -f /environment.yml -n app  
ONBUILD ADD . /app  
  
ENTRYPOINT ["/opt/conda/envs/app/bin/python"]  

