FROM tarhan/python-base:3.5.2-alpine-onbuild  
ONBUILD COPY ./app.yaml /app/  
ONBUILD COPY ./requirements.txt /app/requirements.txt  
ONBUILD RUN /prepare_alpine.sh \  
&& /pip_install.sh \  
&& /postinstall_alpine.sh  
# app.yaml contains two keys 'runtime' and 'buildtime' under
dependencies.alpine key.  
# 'runtime' enlist OS packages contains libraries needed by Python packages  
# to work. For example, lxml Python package uses libxml2 and libxslt libraries  
# at runtime.  
# 'buildtime' enlist OS packages contains header files needed by Python
packages  
# while pip installing them. For example, lxml Python package uses lixml2-dev  
# and libxslt-dev during its installation process. This list does not include  
# standard OS packages needed at build time like gcc or cmake.  
ONBUILD COPY . /app/  
  
ENTRYPOINT ["tini", "--", "scrapy"]  

