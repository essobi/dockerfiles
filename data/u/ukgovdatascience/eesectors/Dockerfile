FROM ubuntu:14.04  
MAINTAINER Matthew Upson  
LABEL date="2017-01-08"  
LABEL version="0.0.0.9002"  
LABEL description="Reproducible Analytical Pipeline environment"  
  
# Update server and install git and R package dependencies  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y git \  
&& apt-get install -y software-properties-common libcurl4-openssl-dev
libxml2-dev libxslt-dev  
  
# Install the current version of R (current is 3.3.2)  
RUN echo "deb http://cloud.r-project.org/bin/linux/ubuntu trusty/" | tee -a
/etc/apt/sources.list > /dev/null \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \  
&& add-apt-repository -y ppa:marutter/rdev \  
&& apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install r-recommended=3.3.2-1trusty0 -y --force-yes \  
&& apt-get install r-base=3.3.2-1trusty0 -y --force-yes \  
&& apt-get install r-base-html=3.3.2-1trusty0 -y --force-yes \  
&& apt-get install r-doc-html=3.3.2-1trusty0 -y --force-yes  
  
# Download latest version of pandoc and install  
RUN curl -L
https://github.com/jgm/pandoc/releases/download/1.18/pandoc-1.18-1-amd64.deb >
pandoc-1.18-1-amd64.deb \  
&& dpkg -i pandoc-1.18-1-amd64.deb \  
&& apt-get install -f  
  
# Copy setup.R file into tea_book  
WORKDIR /RAP  
  
# Clone to RAP-demo-md repo into RAP  
RUN git clone https://github.com/ukgovdatascience/RAP-demo-md.git RAP-demo-md  
  
# Run setup in R to install required packages  
COPY ./setup.R /RAP/  
  
RUN chmod +x setup.R \  
&& Rscript setup.R  
  
#ENTRYPOINT ["Rscript"]  
# List Arguments for compilation (might be better as a script)  
#CMD
["-e","rmarkdown::render(input='index.Rmd',output_format='html_document',output_file='index.html')"]  

