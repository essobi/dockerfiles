FROM anapsix/alpine-java:8 as sdkbuilder  
  
# could use ADD but it always downloads the 137M to check the digest..  
# cool, but for smaller downloads...  
RUN apk add --no-cache curl  
RUN curl -sL https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip -o /sdktools.zip  
RUN mkdir -p /sdk/licenses  
WORKDIR /sdk  
RUN unzip -q /sdktools.zip  
RUN echo 8933bad161af4178b1185d1a37fbf41ea5269c55 > /sdk/licenses/android-sdk-
license  
RUN /sdk/tools/bin/sdkmanager "build-tools;26.0.1"  
WORKDIR /  
RUN curl -sLO https://github.com/pxb1988/dex2jar/releases/download/2.0/dex-
tools-2.0.zip  
RUN unzip -q dex-tools-2.0.zip  
RUN rm dex2jar-2.0/*.bat  
RUN mkdir -p /export/lib/  
RUN curl -sL
https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.2.4.jar >
/export/apktool.jar  
RUN curl -sL
https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool
> /export/apktool  
RUN cp -a /sdk/build-tools/26.0.1/apksigner \  
/sdk/build-tools/26.0.1/zipalign \  
/dex2jar-2.0/* \  
/export/  
RUN cp -a /sdk/build-tools/26.0.1/lib/apksigner.jar \  
/export/lib/  
RUN chmod a+x /export/d2j*.sh  
  
FROM anapsix/alpine-java:8  
RUN mkdir /dedroid/  
COPY \--from=sdkbuilder /export \  
/dedroid/  
COPY \--from=sdkbuilder /sdk/build-tools/26.0.1/lib64/libc++.so /lib64/  
RUN chmod a+x /dedroid/apktool  
COPY entrypoint.sh /entrypoint.sh  
COPY helper.tmpl /helper.tmpl  
COPY allinone /dedroid/allinone  
ENV PATH=/dedroid/:$PATH  
RUN mkdir /work  
WORKDIR /work  
ARG DEDROID="fopina/dedroid"  
ENV DEDROID=$DEDROID  
ENTRYPOINT ["/entrypoint.sh"]

