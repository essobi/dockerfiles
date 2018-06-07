FROM guitarmind/r-base  
MAINTAINER markpeng@exosite.com  
  
RUN apt-get update && apt-get install -y unzip git htop openssh-server
libcurl4-openssl-dev \  
libssl-dev libxml2-dev curl openssl libkrb5-dev libssl1.0.0 libwxbase3.0-0
libwxgtk3.0-0  
  
# install required R dependencies and setup R packages  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile && \  
Rscript -e "install.packages('Rserve')" && \  
Rscript -e "install.packages('zoo')" && \  
Rscript -e "install.packages('xts')" && \  
Rscript -e "install.packages('fpp')" && \  
Rscript -e "install.packages('httr')" && \  
Rscript -e "install.packages('RCurl')" && \  
Rscript -e "install.packages('devtools')" && \  
Rscript -e "devtools::install_version('rjson', version = '0.2.15')" && \  
Rscript -e "install.packages('TSA')" && \  
Rscript -e "devtools::install_github('twitter/AnomalyDetection')" && \  
Rscript -e "install.packages('ggmap')" && \  
Rscript -e "install.packages('data.table')" && \  
Rscript -e "install.packages('tidyverse')" && \  
Rscript -e "install.packages('fasttime')"  
  
# install erlang/elixir dependencies  
ENV OTP_VERSION="19.3.6"  
RUN echo "deb https://packages.erlang-solutions.com/debian jessie contrib" >>
/etc/apt/sources.list && \  
wget https://packages.erlang-solutions.com/debian/erlang_solutions.asc && apt-
key add erlang_solutions.asc && \  
apt-get update && apt-get install -y esl-erlang=1:$OTP_VERSION  
  
# elixir expects utf8.  
ENV ELIXIR_VERSION="v1.4.5" \  
LANG=C.UTF-8  
RUN set -xe \  
&& ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/releases/download/${ELIXIR_VERSION}/Precompiled.zip" \  
&&
ELIXIR_DOWNLOAD_SHA256="a740e634e3c68b1477e16d75a0fd400237a46c62ceb5d04551dbc46093a03f98"\  
&& curl -fSL -o elixir-precompiled.zip $ELIXIR_DOWNLOAD_URL \  
&& echo "$ELIXIR_DOWNLOAD_SHA256 elixir-precompiled.zip" | sha256sum -c - \  
&& unzip -d /usr/local elixir-precompiled.zip \  
&& rm elixir-precompiled.zip \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["iex"]  

