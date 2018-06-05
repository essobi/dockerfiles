# fetch sources  
FROM alpine AS git  
  
WORKDIR /  
  
RUN apk add --update git && \  
git clone https://github.com/sileht/bird-lg.git  
  
# final image  
FROM debian:stretch-slim  
  
ENV LGUID 65534  
ENV LGGID 65534  
EXPOSE 8000  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
python-flask \  
traceroute \  
netbase \  
gunicorn  
  
WORKDIR /bird-lg  
COPY \--from=git /bird-lg /bird-lg  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["lgproxy:app"]  

