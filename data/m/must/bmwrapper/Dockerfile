# TODO: split into two containers, connecting to API over tcp  
FROM must/pybitmessage  
  
RUN locale-gen --no-purge en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
export LANGUAGE=en_US.UTF-8 && \  
export LC_ALL=en_US.UTF-8 && \  
dpkg-reconfigure \--frontend=noninteractive locales  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
ADD . /bmwrapper  
  
ENV pop_port 12344  
ENV smtp_port 12345  
  
EXPOSE $pop_port  
EXPOSE $smtp_port  
  
WORKDIR /bmwrapper  
  
# CMD ["bmwrapper.sh",">/var/log/bmwrapper.log","-l info"]  
  
ENV RUNSH_ARGS "-l debug"  
  
CMD python /PyBitmessage/src/bitmessagemain.py >> /var/log/pybitmessage2.log
2>&1 & $(sleep 5;/bmwrapper/bmwrapper.sh $RUNSH_ARGS)  
ENTRYPOINT []  
# ENTRYPOINT ["bash","bmwrapper.sh",">/var/log/bmwrapper.log"]  

