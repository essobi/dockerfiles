FROM alpine  
ARG HUGO_VERSION="${HUGO_VERSION:-latest}"  
# install tools needed for download  
RUN apk add \--no-cache curl jq  
  
# configure user and working directory  
RUN set -e; \  
addgroup -g 1000 hugo; \  
adduser -u 1000 -G hugo -D hugo; \  
for DIR in "input output"; do \  
mkdir -p "/home/hugo/${DIR}"; \  
chown -R hugo:hugo "/home/hugo/${DIR}"; \  
done;  
USER 1000:1000  
WORKDIR /home/hugo  
  
# install Hugo for `HUGO_VERSION` (from official release tarball)  
RUN set -ex; \  
if [ "${HUGO_VERSION}" = "latest" ]; then \  
api_url='https://api.github.com/repos/gohugoio/hugo/releases/latest'; \  
else \  
api_url="https://api.github.com/repos/gohugoio/hugo/releases/tags/${HUGO_VERSION}";
\  
fi; \  
jq_query='.assets|.[]|select(.name|endswith("Linux-64bit.tar.gz"))|.browser_download_url';
\  
tar_url="$(curl --silent $api_url | jq --raw-output ${jq_query})"; \  
curl --location "${tar_url}" | tar --extract --gzip; \  
test -f hugo; \  
rm LICENSE* README.md  
  
# setup starting environment  
WORKDIR /home/hugo/input  
EXPOSE 1313  
ENTRYPOINT ["/home/hugo/hugo"]  
CMD [ \  
"server", "--watch", "--buildDrafts", \  
"--bind", "0.0.0.0", \  
"--port", "1313", \  
"--baseURL", "http://localhost:1313" \  
]  

