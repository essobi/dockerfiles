FROM rocker/rstudio:latest  
RUN apt-get update && apt-get install -y build-essential \  
ca-certificates \  
gcc \  
git \  
libpq-dev \  
libpng-dev \  
libjpeg-dev \  
libssh2-1-dev \  
make \  
python-pip \  
python2.7 \  
libxml2-dev \  
zlib1g-dev \  
xzdec \  
texlive \  
texlive-xetex \  
texlive-xetex \  
texlive-luatex \  
texlive-lang-cjk \  
texlive-lang-korean \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Python Dependencies  
RUN pip install feather-format pandas  
  
# LaTeX Korean Support  
RUN tlmgr init-usertree \  
&& tlmgr repository add http://ftp.ktug.org/KTUG/texlive/tlnet ktug \  
&& tlmgr pinning add ktug "*"  
  
RUN Rscript -e "install.packages('devtools', dep = T);
devtools::install_github('csgillespie/efficient', dep = T)"  
  
ADD . /code  
WORKDIR /code  
  
RUN Rscript -e "devtools::install_deps('.')" && R CMD INSTALL ../code  
  
VOLUME /code  
CMD make clean && make html  

