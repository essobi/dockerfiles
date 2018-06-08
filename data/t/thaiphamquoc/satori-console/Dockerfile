FROM node:8.4.0  
MAINTAINER tpham  
  
USER root  
ARG ssh_dir=/root/.ssh  
ARG work_dir=/projects  
ARG argus_ui_version="0.0.3"  
RUN mkdir ${ssh_dir} && \  
chmod 640 ${ssh_dir}  
  
COPY ssh/config ${ssh_dir}/config  
COPY ssh/id_rsa ${ssh_dir}/id_rsa  
COPY ssh/id_rsa.pub ${ssh_dir}/id_rsa.pub  
  
RUN chmod 640 ${ssh_dir}/config && \  
chmod 600 ${ssh_dir}/id_rsa && \  
chmod 640 ${ssh_dir}/id_rsa.pub  
  
WORKDIR ${work_dir}  
RUN git clone --branch ${argus_ui_version}
git@bitbucket.org:thaiphamquoc/argus-ui.git  
WORKDIR ${work_dir}/argus-ui  
  
ENTRYPOINT ["/projects/argus-ui/scripts/start-up.sh"]  
  
EXPOSE 3000  

