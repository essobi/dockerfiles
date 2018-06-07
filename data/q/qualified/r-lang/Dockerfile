FROM buildpack-deps:xenial  
  
# https://cran.r-project.org/bin/linux/ubuntu/README  
RUN set -ex; \  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9; \  
gpg -a --export E084DAB9 | apt-key add -; \  
echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list; \  
apt-get -q update; \  
apt-get -q -y --no-install-recommends install 'r-base=3.4.*' 'r-base-
dev=3.4.*'; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/*;  
  
RUN set -ex; \  
R -q -e 'install.packages("devtools", repo="https://cran.rstudio.com/")'; \  
# https://github.com/r-lib/testthat  
# testthat 2.0.0  
R -q -e 'devtools::install_version("testthat", version = "2.0.0", repos =
"https://cran.rstudio.com")'; \  
# https://www.tidyverse.org/  
# tidyverse 1.2.1  
# core packages:  
# - ggplot2: data visualisation  
# - dplyr: data manipulation  
# - tidyr: data tidying  
# - readr: data import  
# - purrr: functional programming  
# - tibble: modern re-imagining of data frames  
# - stringr: strings  
# - forcats: factors  
R -q -e 'devtools::install_version("tidyverse", version = "1.2.1", repos =
"https://cran.rstudio.com")'; \  
# install svglite so `ggsave` can produce SVG  
R -q -e 'devtools::install_version("svglite", version = "1.2.1", repos =
"https://cran.rstudio.com")'; \  
rm -rf /tmp/*;  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
WORKDIR /workspace  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

