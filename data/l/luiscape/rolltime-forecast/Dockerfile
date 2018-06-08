############################################################  
# Container that runs the Rolltime Forecast micro-service. #  
# It needs a performant R instance. Receive links from DB. #  
############################################################  
  
FROM ubuntu:trusty  
  
USER root  
  
#  
# Setting up basic Ubuntu  
# machine with R.  
#  
RUN \  
apt-get install -y software-properties-common \  
&& sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com E084DAB9 \  
&& sudo add-apt-repository "deb http://cran.cnr.Berkeley.edu/bin/linux/ubuntu
trusty/" \  
&& sudo apt-get update \  
&& apt-get install -y postgresql-client libpq-dev \  
&& sudo apt-get install -y r-base r-base-dev \  
&& sudo apt-get install -y libcurl4-openssl-dev libxml2-dev \  
&& sudo apt-get install -y git  
  
#  
# Cloning repository and  
# setting-up the application.  
#  
RUN \  
git clone http://github.com/rolltime/rolltime-forecast \  
&& cd rolltime-forecast \  
&& echo "install.packages('packrat', repos='http://cran.rstudio.com/')" | R
--no-save \  
&& make setup  
  
WORKDIR "/rolltime-forecast"  
  
EXPOSE 6000  
  
CMD ["make", "run"]  

