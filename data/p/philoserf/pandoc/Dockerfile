FROM debian:sid-slim  
LABEL maintainer "Mark Ayers <mark@philoserf.com>"  
  
WORKDIR /var/tmp  
  
RUN apt-get update -y\  
&& apt-get upgrade -y\  
&& apt-get dist-upgrade -y\  
&& apt-get install -y curl\  
&& rm -rf /var/lib/apt/lists/*  
  
ENV VERSION 2.2.1  
ENV PANDOC_URL
https://github.com/jgm/pandoc/releases/download/${VERSION}/pandoc-${VERSION}-1-amd64.deb  
ENV PANDOC_PKG pandoc.deb  
  
RUN curl -sL ${PANDOC_URL} -o ${PANDOC_PKG} \  
&& dpkg -i ${PANDOC_PKG} \  
&& rm -rf ${PANDOC_PKG}  
  
ENTRYPOINT ["pandoc"]  
CMD ["--help"]  

