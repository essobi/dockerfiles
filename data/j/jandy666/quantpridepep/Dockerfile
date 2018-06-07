FROM continuumio/anaconda  
  
RUN apt-get update  
RUN conda install numpy pandas scikit-learn  
RUN pip install argparse pymzML==0.7.8  
RUN pip install simplejson  
RUN apt-get install git  
RUN apt-get update -y  
RUN apt-get install gnupg -y  
  
RUN apt-get update -y  
RUN apt-get install openjdk-8-jdk-headless -y  
RUN apt-get clean  
  
RUN apt-get install parallel -y  
  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy-
apache24-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian stable-stretch
main" | tee /etc/apt/sources.list.d/mono-official.list  
RUN apt-get update  
RUN apt-get install mono-complete -y  
RUN git clone -b master --single-branch https://github.com/compomics/moff
/moFF  
RUN git clone -b master --single-branch
https://github.com/compomics/QuantPridePep.git /moFF_pipeline  
  
WORKDIR /moFF_pipeline  

