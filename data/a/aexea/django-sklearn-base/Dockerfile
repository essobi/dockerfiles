FROM aexea/aexea-base:py3.6-stretch  
LABEL maintainer "Aexea Carpentry"  
  
EXPOSE 8000  
RUN pip3 install psycopg2 lxml Pillow pandas wheel numpy  
  
# scipy / scikit-learn  
RUN apt-get update && apt-get -y upgrade && apt-get install -y libblas-dev
liblapack-dev libatlas-base-dev gfortran  
  
# keras  
ENV KERAS_BACKEND tensorflow  
  
# hunspell  
RUN apt-get update && apt-get install -y libhunspell-dev libicu-dev unzip  
  
ONBUILD COPY requirements*.txt /opt/code/  
ONBUILD COPY pip.conf /root/.config/pip/pip.conf  
ONBUILD WORKDIR /opt/code  
ONBUILD RUN pip3 install -Ur requirements.txt \  
&& if test -e requirements-deploy.txt; then \  
pip3 install -Ur requirements-deploy.txt; \  
fi  
  
ONBUILD ADD . /opt/code  
ONBUILD WORKDIR /opt/code  
ONBUILD USER uid1000  

