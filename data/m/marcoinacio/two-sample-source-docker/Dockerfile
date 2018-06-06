FROM ubuntu  
  
MAINTAINER Marco Inacio <dockerfiles@marcoinacio.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y apt-utils && \  
apt-get dist-upgrade -y && \  
apt-get install -y \  
nano build-essential python3 python3-pip r-base python3-tk \  
python3-rpy2 && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install npcompare pandas pystan matplotlib sklearn  
  
RUN mkdir /workdir /workdir2  
WORKDIR /workdir  
ADD files/ /workdir2  
  
#Set default backend for matplotlib  
#Prevents complaing about undefined $DISPLAY  
ENV MPLCONFIGDIR /workdir  
RUN echo "backend : Agg" > /workdir2/matplotlibrc  
  
CMD \  
mv /workdir2/* /workdir && \  
mkdir -p plots && mkdir -p results && mkdir -p results/metric && \  
mkdir -p results/mixture && \  
R CMD BATCH fourier.R && \  
python3 plot_gaussian_densities.py && \  
\  
python3 runsampler.py type 1 && \  
python3 runsampler.py type 2 && \  
python3 runsampler.py type 3 && \  
\  
bash -c "python3 runmetric.py type 1 2 & \  
python3 runmetric.py type 1 3 & \  
python3 runmetric.py type 2 3 & \  
python3 runmetric.py type 1 1 & \  
python3 runmetric.py type 2 2 & \  
python3 runmetric.py type 3 3 & \  
wait" && \  
\  
python3 runmetric_plots.py && \  
\  
python3 generate_dataset.py && \  
python3 runsampler.py type real && \  
python3 runmetric.py type real real && \  
\  
tail -F /dev/null  
  
#Obs.: Dataset with real data used on the article cannot be shared  
#publicly  
#Here we are using other dataset with randomly generated data  

