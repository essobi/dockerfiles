FROM bioboxes/validator-base  
MAINTAINER Michael Barton, mail@michaelbarton.me.uk  
  
ENV PACKAGES wget xz-utils  
RUN apt-get install -y --no-install-recommends ${PACKAGES}  
  
ADD mount/features /root/features/  
ADD mount/Makefile /root/Makefile  
ADD mount/schema /root/schema  
WORKDIR /root  
RUN make bootstrap  
  
#install  
ENV BASE_URL https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-
biobox-file  
ENV VERSION 0.x.y  
ENV DEST /root/bin  
RUN mkdir ${DEST}  
RUN wget \  
\--quiet \  
\--output-document -\  
${BASE_URL}/${VERSION}/validate-biobox-file.tar.xz \  
| tar xJf - \  
\--directory ${DEST} \  
\--strip-components=1  
  
ENV PATH ${PATH}:${DEST}  
  
CMD ["/root/run"]  

