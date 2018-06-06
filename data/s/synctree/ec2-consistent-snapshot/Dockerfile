FROM synctree/bases:ubuntu-12.04-deploy-latest  
  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository ppa:alestic  
RUN apt-get update -y  
RUN apt-get install -y ec2-consistent-snapshot  
RUN curl -L http://cpanmin.us | perl - --self-upgrade  
RUN cpanm install MongoDB  
RUN cpanm install Any::Moose MongoDB::Admin  

