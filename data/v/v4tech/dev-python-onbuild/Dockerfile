FROM v4tech/dev-python:latest  
MAINTAINER Stewart V. Wright <stewart@vifortech.com>  
  
# These commands run when a new image is built  
ONBUILD ADD .condarc /root/.condarc  
ONBUILD ADD wanted-py-packages.txt /wanted-py-packages.txt  
# Check to see there is some file to install...  
ONBUILD RUN if [ 0$(grep -cve '^#' -e '^$' /wanted-py-packages.txt) -gt 0 ];
then \  
conda install --yes --file /wanted-py-packages.txt; \  
fi  
ONBUILD ADD . /app  
  
#ENTRYPOINT ["/opt/conda/bin/python"]  

