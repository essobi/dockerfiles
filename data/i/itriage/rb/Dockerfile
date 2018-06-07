FROM itriage/base  
MAINTAINER Itriage Ops <ops@itriagehealth.com>  
  
# Setup the Environment  
ENV PATH /rubies/current/bin:/rubies/support/bin:$PATH  
ENV BUILD_HOST http://ruby.itri.ag  
ENV HOME /settings  
ADD settings /settings  
  
# Add the support files  
ADD support /rubies/support  
RUN chmod +x /rubies/support/bin/*  
  
# Install the latest ruby  
ADD .ruby-version .ruby-version  
RUN install-ruby  
  
# Install ruby on children  
ONBUILD RUN rm -rf /rubies/versions  
ONBUILD ADD .ruby-version /.ruby-version  
ONBUILD RUN install-ruby  
ONBUILD ADD . /mnt/app  
ONBUILD WORKDIR /mnt/app  

