FROM shuewe/docker-download-folderstructure  
  
MAINTAINER Stephan Hüwe (shuewe87@gmail.com)  
  
#Resources  
ADD scripts scripts  
ADD setup setup  
  
#python modules  
RUN python -m pip install numpy keras sklearn pandas matplotlib tensorflow
requests jupyter h5py  
  
#Replace matplotlib configuration to enable plots in docker  
RUN cp /setup/matplotlibrc /usr/local/lib/python3.6/dist-
packages/matplotlib/mpl-data/matplotlibrc  
  
RUN ["chmod", "+x", "/scripts/start.sh"]  
  
#For jupyter expose port (has to be enabled with --jupyter as entrypoint
option)  
EXPOSE 8888  
ENTRYPOINT ["/scripts/start.sh"]  

