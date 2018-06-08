FROM flowerseems/debian-base  
  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 build-
essential git  
RUN wget https://repo.continuum.io/archive -O - 2>/dev/null | grep Anaconda2 |
grep x86_64 | head -1 | awk -F '"' '{print $2}' |{ read uri; wget
"https://repo.continuum.io/archive/${uri}" -O ~/anaconda2.sh -c -t 0; }  
RUN /bin/bash ~/anaconda2.sh -b -p /opt/conda  
RUN rm -f ~/anaconda2.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
# notebook  
#RUN /opt/conda/bin/conda install jupyter -y --quiet  
RUN conda install jupyter -y --quiet  
RUN conda install -y -c conda-forge jupyter_contrib_nbextensions bcolz  
  
# theano  
RUN conda install theano -y --quiet  
RUN mkdir /opt/notebooks  
  
# tensorflow  
RUN conda install keras -y  
RUN pip install --ignore-installed --upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.3.0-cp27-none-
linux_x86_64.whl  
  
RUN apt-get purge --auto-remove -y wget  
RUN rm -rf /var/cache/apk/*  
  
ENV NOTEBOOK_PASSWORD
'sha1:5e784f269734:9c3ea0d0ade73881b3b1ff8282f4c23252a95adc'  
CMD /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*'
\--port=8888 --no-browser --NotebookApp.password_required=True
--NotebookApp.password=$NOTEBOOK_PASSWORD \--allow-root  
  

