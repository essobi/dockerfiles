FROM xueshanf/s3fs  
MAINTAINER Chris Fordham <chris@fordham-nagy.id.au>  
  
# USAGE  
# $ docker build -t s3-backed-ftp-server .  
# $ docker run s3-backed-ftp-server  
# or detached, with user/pass (ftp/ftp) and port forward:  
# docker run -itd \  
# --cap-add mknod \  
# --cap-add sys_admin \  
# --device=/dev/fuse \  
# -p 21:21 \  
# -p 15393-15592:15393-15592 \  
# -e S3_BUCKET=starbug-tandoori \  
# -e AWS_ACCESS_KEY_ID=AKIA...I4Q \  
# -e 'AWS_SECRET_ACCESS_KEY=X3p...lK1' \  
# -e FTP_USER=vftp \  
# -e FTP_PASSWORD='$1$qSvGek8Y$r4xPYlK5lCWhuVxdfKvf7.' \  
# s3-backed-ftp-server  
# tag and push  
# $ docker tag s3-backed-ftp-server flaccid/s3-backed-ftp-server  
# $ docker push flaccid/s3-backed-ftp-server  
RUN groupadd -g 48 ftp && \  
useradd --no-create-home --home-dir /srv -s /bin/false \--uid 48 --gid 48 -c
'ftp daemon' ftp  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends vsftpd db5.3-util \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/run/vsftpd/empty /etc/vsftpd/user_conf /var/ftp /srv && \  
touch /var/log/vsftpd.log && \  
rm -rf /srv/ftp  
  
COPY vsftpd*.conf /etc/  
COPY vsftpd_virtual /etc/pam.d/  
COPY *.sh /  
  
VOLUME ["/etc/vsftpd", "/srv"]  
  
EXPOSE 21  
EXPOSE 22  
EXPOSE 15393-15592  
ENTRYPOINT ["/entry.sh"]  
CMD ["vsftpd"]  

