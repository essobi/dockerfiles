FROM alpine:latest  
  
RUN apk --update --no-cache add \  
git \  
bash \  
python3 \  
gcc \  
make \  
libffi-dev \  
python3-dev \  
linux-headers \  
musl-dev \  
openssl-dev \  
&& pip3 install virtualenv \  
&& git clone https://git.openstack.org/openstack/tempest  
WORKDIR /tempest  
RUN pip3 install -e .  
  
WORKDIR /tempest_env  
RUN tempest init  
  
CMD [ "bash", "-c", "mkdir -p workspaces; cd workspaces; tempest workspace
remove --name cloud01 --rmdir; tempest init cloud01 && cd cloud01 && tempest
run -l" ]  

