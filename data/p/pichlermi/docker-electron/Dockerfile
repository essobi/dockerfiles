FROM williamyeh/ansible:ubuntu16.04  
  
WORKDIR /app  
  
ARG user_name=user  
ARG user_group=user  
ARG user_id=1000  
ARG user_gid=1000  
  
COPY ./ansible/. /ansible  
  
RUN echo localhost > inventory && \  
ansible-playbook -i inventory \  
/ansible/electron-docker.yml \  
\--connection=local \  
\--extra-vars="\  
app_dir=/app \  
user_name=$user_name \  
user_group=$user_group \  
user_id=$user_id \  
user_gid=$user_gid" && \  
rm inventory && \  
rm -rf /ansible  
  
USER $user_name  
WORKDIR /app  
  

