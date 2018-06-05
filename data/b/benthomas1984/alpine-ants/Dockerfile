# ANTs  
  
FROM benthomas1984/alpine-itk:4.12.1  
  
MAINTAINER Benjamin A. Thomas <b.a.thomas@ucl.ac.uk>  
LABEL Description="ANTs" Version="2.2.0"  
  
RUN apk --update add ca-certificates && apk upgrade && apk add bash  
  
RUN mkdir -p /opt/ANTS/BUILD && cd /opt/ANTS && \  
git clone -b 'v2.2.0' \--single-branch --depth=1
https://github.com/stnava/ANTs.git && \  
cd /opt/ANTS/BUILD && \  
cmake -DCMAKE_BUILD_TYPE:STRING=Release -DUSE_SYSTEM_ITK:BOOL=ON
-DBUILD_TESTING:BOOL=OFF -DBUILD_EXAMPLES:BOOL=OFF /opt/ANTS/ANTs && \  
make && cp /opt/ANTS/ANTs/Scripts/* /opt/ANTS/BUILD/bin && rm -rf
/opt/ANTS/BUILD/ANTS-build  
  
ENV ANTSPATH=/opt/ANTS/BUILD/bin  
ENV PATH="${ANTSPATH}:${PATH}"  

