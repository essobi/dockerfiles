FROM sequenceiq/spark:1.5.1  
MAINTAINER LOGBASE  
  
#Install Anaconda  
RUN curl -s
https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.3.0-Linux-x86_64.sh
-o anaconda.sh  
RUN chmod a+x anaconda.sh  
RUN ./anaconda.sh -b  
RUN ./anaconda3/bin/conda install -y -q ipython notebook  
  
#Environment vaiables for Spark to use Anaconda Python and iPython notebook  
ENV PYSPARK_PYTHON /anaconda3/bin/python3  
ENV PYSPARK_DRIVER_PYTHON /anaconda3/bin/ipython3  
ENV PYSPARK_DRIVER_PYTHON_OPTS "notebook --no-browser --port=8888 --ip='*'"  
#iPython port  
EXPOSE 8888  
#Spark port  
EXPOSE 4040  
CMD ["pyspark"]  

