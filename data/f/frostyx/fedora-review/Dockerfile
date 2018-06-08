FROM fedora:latest  
  
RUN dnf -y install fedora-review vim && dnf -y clean all  
  
# Mock inside of a docker required configuration  
ENV REVIEW_NO_MOCKGROUP_CHECK False  
RUN echo 'config_opts["use_nspawn"] = False' >> /etc/mock/site-defaults.cfg  
  
# So the review directory is not created right in the /  
RUN mkdir /review  
WORKDIR /review  

