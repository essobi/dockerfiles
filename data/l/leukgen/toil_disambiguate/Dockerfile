FROM leukgen/docker-pcapcore:v0.1.1  
# install packages dependencies  
RUN apt-get update -yqq \  
&& apt-get install -yqq python python-pip \  
&& apt-get clean \  
&& pip install --upgrade pip  
  
# use existing htslib for pysam, see leukgen/docker-pcapcore  
ENV HTSLIB_LIBRARY_DIR=$OPT/lib  
ENV HTSLIB_INCLUDE_DIR=$OPT/include  
  
# mount the output volume as persistant  
ENV OUTPUT_DIR /data  
VOLUME ${OUTPUT_DIR}  
  
# install toil_disambiguate  
COPY . /code  
RUN pip install /code && rm -rf /code  
  
# add entry point  
ENTRYPOINT ["toil_disambiguate"]  

