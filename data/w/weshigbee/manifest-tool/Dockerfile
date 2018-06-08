FROM buildpack-deps:curl  
  
ENV MANIFEST_TOOL_VERSION=v0.4.0  
ENV DOWNLOAD_URL=https://github.com/estesp/manifest-
tool/releases/download/${MANIFEST_TOOL_VERSION}/manifest-tool-linux-amd64  
  
RUN curl -L -o /manifest-tool ${DOWNLOAD_URL} \  
&& chmod +x /manifest-tool  
  
ENTRYPOINT ["/manifest-tool"]  

