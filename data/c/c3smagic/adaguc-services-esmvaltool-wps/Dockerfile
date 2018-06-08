from c3smagic/adaguc-services  
  
#Install ESMValTool  
# install conda  
RUN curl -L -O https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh  
RUN bash ./Miniconda2-latest-Linux-x86_64.sh -p /miniconda -b  
ENV PATH=/miniconda/bin:${PATH}  
RUN conda update -y conda  
RUN conda update -y pip  
  
# install python packages specified in conda environment file  
COPY environment.yml /src/environment.yml  
WORKDIR /src/  
RUN conda env update -f environment.yml  
  
# install esmvaltool  
#master branch  
#RUN curl -L -O https://github.com/c3s-magic/ESMValTool/archive/master.zip  
#RUN unzip master.zip  
#RUN mv /src/ESMValTool-master /src/ESMValTool/  
#mult-instance-quickfix branch  
RUN curl -L -O https://github.com/c3s-magic/ESMValTool/archive/multi-instance-
quickfix.zip  
RUN unzip multi-instance-quickfix.zip  
RUN mv /src/ESMValTool-multi-instance-quickfix /src/ESMValTool/  
  
WORKDIR /src/ESMValTool  
COPY config_private.xml /src/ESMValTool/config_private.xml  
  
#copy namelists into container  
RUN mkdir -p /namelists  
COPY namelists /namelists/  
  
#copy wps processes into container  
COPY processes /src/processes/  
  
#To get a working env: Set PATH to
/miniconda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
WORKDIR /src/adaguc-services  
  
# Normally this container is run as an adaguc services.  
# To run esmvaltool with this container instead, uncomment the following
lines.  
#WORKDIR /src/ESMValTool  
#ENTRYPOINT ["python", "main.py"]  
#CMD ["nml/namelist_test.xml"]  

