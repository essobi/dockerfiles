FROM hermsi/alpine-fpm-php  
  
LABEL maintainer "https://github.com/hermsi1337"  
# Get some stuff in order to work properly  
RUN apk --no-cache --update --virtual .build-dependencies add gnupg openssl
wget zip \  
&& update-ca-certificates  
  
# Download and install RainLoop  
ENV RAINLOOP_ROOT="/rainloop"  
ARG GPG_FINGERPRINT="3B79 7ECE 694F 3B7B 70F3 11A4 ED7C 49D9 87DA 4591"  
RUN export TMP_DIR="/tmp" && \  
export RAINLOOP_ZIP="${TMP_DIR}/RainLoop.zip" && \  
export RAINLOOP_ZIP_ASC="${RAINLOOP_ZIP}.asc" && \  
export RAINLOOP_ASC="${TMP_DIR}/RainLoop.asc" && \  
wget -q "https://www.rainloop.net/repository/webmail/rainloop-community-
latest.zip" -O "${RAINLOOP_ZIP}" && \  
wget -q "https://www.rainloop.net/repository/webmail/rainloop-community-
latest.zip.asc" -O "${RAINLOOP_ZIP_ASC}" && \  
wget -q "https://www.rainloop.net/repository/RainLoop.asc" -O
"${RAINLOOP_ASC}" && \  
gpg --import "${RAINLOOP_ASC}" && \  
FINGERPRINT="$(LANG=C gpg --verify ${RAINLOOP_ZIP_ASC} ${RAINLOOP_ZIP} 2>&1 \  
| sed -n "s#Primary key fingerprint: \\(.*\\)#\1#p")" && \  
if [ -z "${FINGERPRINT}" ]; then echo "Warning! Invalid GPG signature!" &&
exit 1; fi && \  
if [ "${FINGERPRINT}" != "${GPG_FINGERPRINT}" ]; then echo "Warning! Wrong GPG
fingerprint!" && exit 1; fi && \  
mkdir "${RAINLOOP_ROOT}" && \  
unzip -q "${RAINLOOP_ZIP}" -d "${RAINLOOP_ROOT}" && \  
apk del .build-dependencies && \  
rm -rf "${TMP_DIR}/*" "/var/cache/apk/*" "/root/.gnupg"  
# Take care of additional configuration stuff  
ENV MEMORY_LIMIT="128M" \  
UPLOAD_MAX_FILESIZE="32M" \  
POST_MAX_SIZE="64M"  
RUN chown "www-data." "${RAINLOOP_ROOT}" -R && \  
find "${RAINLOOP_ROOT}" -type d -exec chmod 755 {} \; && \  
find "${RAINLOOP_ROOT}" -type f -exec chmod 644 {} \; && \  
printf "%s\n%s\n%s" "memory_limit = ${MEMORY_LIMIT}" "upload_max_filesize =
${UPLOAD_MAX_FILESIZE}" "post_max_size = ${POST_MAX_SIZE}" >
"${RAINLOOP_ROOT}/.user.ini"; \  

