FROM fusordevel/atomicapp  
  
MAINTAINER Dylan Murray <dymurray@redhat.com>  
  
LABEL io.projectatomic.nulecule.specversion="0.0.2" \  
io.projectatomic.nulecule.providers="kubernetes, openshift, docker" \  
Build="docker build --rm --tag test/wordpress-atomicapp ."  
  
ADD /Nulecule /Dockerfile README.md /application-entity/  
ADD /artifacts /application-entity/artifacts  

