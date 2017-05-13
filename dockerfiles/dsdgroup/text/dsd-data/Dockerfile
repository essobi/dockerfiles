FROM atmoz/sftp

MAINTAINER Guo Quan <guoquanscu@gmail.com>

ENV REFRESHED_AT 2016-11-01
EXPOSE 22
# volumes
VOLUME ["/home/dsddata/data"]

# startup
CMD ["dsddata:dsddata:::data"]
