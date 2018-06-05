FROM opencpu/base:latest  
MAINTAINER Steve Nolen <technolengy@gmail.com>  
  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone \--single-branch https://github.com/mobilizingcs/plotapp
/tmp/plotbuilder  
  
RUN /usr/bin/R -e 'install.packages(c("Ohmage", "ggplot2", "curl",
"rstudioapi"), repo = "https://cran.rstudio.com")'  
WORKDIR /tmp  
RUN /usr/bin/R CMD INSTALL plotbuilder --library=/usr/local/lib/R/site-library  
  
EXPOSE 80  
ADD docker_entrypoint.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD service opencpu restart && tail -F /var/log/opencpu/apache_access.log

