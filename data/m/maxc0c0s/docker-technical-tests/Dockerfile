FROM ubuntu:14.04  
MAINTAINER Sebastien Delisle <seb0del@gmail.com>  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes python-
virtualenv git  
  
RUN useradd -m cm_user  
  
RUN mkdir -p /entry_point_script  
COPY cloud_manager_cmd.sh /entry_point_script/  
RUN chown -R cm_user:cm_user /entry_point_script  
  
RUN git clone https://github.com/maxc0c0s/technical_tests.git  
RUN chown -R cm_user:cm_user /technical_tests  
  
RUN virtualenv /technical_tests_env  
RUN chown -R cm_user:cm_user /technical_tests_env  
  
EXPOSE 8000  
USER cm_user  
  
ENTRYPOINT ["/entry_point_script/cloud_manager_cmd.sh"]  

