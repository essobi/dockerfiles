FROM fedora:rawhide  
  
RUN yum clean all && yum -y update && yum -y install devassistant-cli
python3-jsonschema && yum clean all  
RUN useradd dev  
  
VOLUME /home/dev  
VOLUME /project  
RUN chown dev:dev -R /project  
WORKDIR /project  
RUN da pkg install nulecule  
  
USER dev  
  
LABEL RUN docker run -d --privileged -u `id -u $USER` -v `echo
$HOME`:/home/dev -v `pwd`:/project --name NAME -e NAME=NAME -e IMAGE=IMAGE
--entrypoint=bash IMAGE -c \"tail -f /dev/null\"  
  
LABEL USER_RUN docker run -it --rm --privileged --name da -u `id -u $USER` -v
`echo $HOME`:/home/dev -v `pwd`:/project IMAGE  
  
ENTRYPOINT ["/usr/bin/da"]  

