FROM zappi/kubectl:1.5.3-1  
RUN addgroup -g 9999 visualizer  
RUN adduser -S -D -u 9999 -G visualizer visualizer  
  
ARG K8S_VISUALIZER_VERSION="fdfd7db7ce9a670411b4a3c0e2b65c8a77eb184d"  
ARG K8S_VISUALIZER_PKG="${K8S_VISUALIZER_VERSION}.zip"  
ARG
K8S_VISUALIZER_SHA="0db4f80503e3c3cc2fbabe9e94f07ea7e96b9906547c3257f39870158417c87d"  
RUN cd /srv && \  
wget --show-progress "https://github.com/saturnism/gcp-
live-k8s-visualizer/archive/${K8S_VISUALIZER_PKG}" && \  
echo "${K8S_VISUALIZER_SHA} *${K8S_VISUALIZER_PKG}" | sha256sum -c - && \  
unzip "${K8S_VISUALIZER_PKG}" && \  
mv "gcp-live-k8s-visualizer-${K8S_VISUALIZER_VERSION}" "kubernetes-visualizer"
&& \  
rm "/srv/${K8S_VISUALIZER_PKG}"  
WORKDIR "/srv/kubernetes-visualizer"  
  
USER visualizer  
ENV HOME /home/visualizer  
  
EXPOSE 8001  
CMD ["proxy", "--www=.", "--address=0.0.0.0", "--www-prefix=/visualizer/"]  

