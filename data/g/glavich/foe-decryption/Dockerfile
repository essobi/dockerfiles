FROM alpine:latest  
LABEL maintainer="Glavić <glavic@gmail.com>"  
  
ENV \  
FOE_DECRYPTION_PATH=/foe-decryption \  
FFDEC_PATH=/ffdec  
  
RUN \  
apk update --quiet && \  
apk upgrade --quiet && \  
apk add --quiet python git curl unzip bash openjdk8-jre  
  
RUN \  
mkdir ${FOE_DECRYPTION_PATH} && \  
cd ${FOE_DECRYPTION_PATH} && \  
git clone \--quiet https://github.com/Glavic/foe-decryption.git . && \  
git checkout Docker && \  
chmod +x script.sh  
  
RUN \  
mkdir ${FFDEC_PATH} && \  
cd ${FFDEC_PATH} && \  
FFDEC_URL=$( \  
curl -s https://api.github.com/repos/jindrapetrik/jpexs-
decompiler/releases/latest \  
| grep "browser_download_url.*zip" \  
| head -n 1 \  
| cut -d : -f 2,3 \  
| tr -d '[:space:]"' \  
) && \  
curl -s -L -o ffdec.zip ${FFDEC_URL} && \  
unzip -qq ffdec.zip && \  
chmod +x ffdec.sh  
  
CMD ${FOE_DECRYPTION_PATH}/script.sh  

