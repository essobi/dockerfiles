FROM frolvlad/alpine-gcc:latest  
  
# Metadata  
LABEL base.image="frolvlad/alpine-gcc:latest"  
LABEL version="2.3.4"  
LABEL software="structure"  
LABEL software.version="2.3.4"  
LABEL description="Structure is a free software package for using multi-locus
genotype data to investigate population structure."  
LABEL website="http://web.stanford.edu/group/pritchardlab/structure.html"  
LABEL
documentation="http://web.stanford.edu/group/pritchardlab/structure.html"  
LABEL license="http://web.stanford.edu/group/pritchardlab/structure.html"  
LABEL tags="Population Genetics"  
  
# Maintainer  
MAINTAINER André M. Ribeiro dos Santos <andremrsantos@gmail.com>  
  
ENV VERSION 2.3.4  
RUN apk update && apk add --no-cache curl make \  
&& curl -sL
http://web.stanford.edu/group/pritchardlab/structure_software/release_versions/v${VERSION}/structure_kernel_source.tar.gz
| tar xz \  
&& mv structure_kernel_src src && cd src && make \  
&& rm -rf /var/cache/apk/* \  
&& adduser -D -u 1000 structure \  
&& mkdir /structure \  
&& chown -R structure /structure  
  
ENV PATH /src:$PATH  
  
USER structure  
WORKDIR /structure  
  
CMD ["/src/structure"]  

