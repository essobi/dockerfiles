# AWS X-Ray v2.1  
#  
# docker run --rm pottava/xray:2.1 --help  
# docker run --name xray -d -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY \  
# -p 2000:2000/udp pottava/xray:2.1 --region ${AWS_REGION} --local-mode  
FROM alpine:3.7  
  
ENV XRAY_VERSION=2.1.0  
  
RUN apk --no-cache add ca-certificates  
RUN apk --no-cache add \--virtual build-dependencies bash curl libgcc unzip
gpgme \  
  
# Install GNU libc  
&& GLIBC_VERSION=2.27-r0 \  
&& GLIBC_DL_URL="https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}" \  
&& curl --location --silent --show-error -O
${GLIBC_DL_URL}/glibc-${GLIBC_VERSION}.apk \  
&& curl --location --silent --show-error -O ${GLIBC_DL_URL}/glibc-
bin-${GLIBC_VERSION}.apk \  
&& curl --location --silent --show-error -O
${GLIBC_DL_URL}/glibc-i18n-${GLIBC_VERSION}.apk \  
&& apk add \--allow-untrusted glibc-${GLIBC_VERSION}.apk \  
glibc-bin-${GLIBC_VERSION}.apk glibc-i18n-${GLIBC_VERSION}.apk \  
&& /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib \  
&& /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& rm -rf glibc-${GLIBC_VERSION}.apk \  
glibc-bin-${GLIBC_VERSION}.apk glibc-i18n-${GLIBC_VERSION}.apk \  
  
# Install AWS X-Ray daemon  
&& cd /usr/lib \  
&& xray_url=https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-
east-2/xray-daemon \  
&& xray_zip=aws-xray-daemon-linux-${XRAY_VERSION}.zip \  
&& curl -O --location --silent --show-error ${xray_url}/${xray_zip} \  
&& curl -O --location --silent --show-error ${xray_url}/${xray_zip}.sig \  
&& curl --location --silent --show-error ${xray_url}/aws-xray.gpg | gpg
--import \  
&& gpg --verify ${xray_zip}.sig ${xray_zip} \  
&& unzip -q ${xray_zip} \  
&& rm -rf ${xray_zip} ${xray_zip}.sig \  
&& ln -s /usr/lib/xray /usr/bin/ \  
&& ln -sf /dev/stdout /var/log/xray-daemon.log \  
  
&& apk del --purge -r build-dependencies  
  
ADD xray-daemon.yaml /  
  
EXPOSE 2000/udp  
  
ENTRYPOINT ["xray", "--config", "/xray-daemon.yaml"]  
CMD ["--region", "us-west-2"]  

