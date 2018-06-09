FROM buildpack-deps  
  
RUN apt-get update  
RUN apt-get install cmake -y  
  
WORKDIR /root  
  
RUN git clone \--depth 1 https://github.com/h2o/h2o \  
&& cd h2o \  
&& git submodule update --init --recursive \  
&& cmake -DWITH_BUNDLED_SSL=on . \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf h2o  
  
ADD run.sh run.sh  
  
CMD ["./run.sh"]  

