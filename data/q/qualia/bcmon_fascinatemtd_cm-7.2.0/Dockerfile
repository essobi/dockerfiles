# BUILD-USING: docker build -t qualia/bcmon_fascinatemtd_cm-7.2.0 .  
# RUN-USING: docker run -name fascinatemtd qualia/bcmon_fascinatemtd_cm-7.2.0
&& docker wait fascinatemtd && docker cp
fascinatemtd:/root/kernel/drivers/net/wireless/bcm4329/bcm4329.ko . && docker
rm fascinatemtd  
FROM qualia/bcmon_base  
MAINTAINER Drew Carey Buglione <me@drewb.ug>  
  
RUN git clone https://github.com/CyanogenMod/android_kernel_samsung_aries.git
--branch android-samsung-2.6.35 kernel && \  
cd kernel && \  
git reset --hard 9f2f56ba61088176b9c7b41d4fe3f5d26658f58f  
  
WORKDIR root/kernel  
  
RUN rm -r drivers/net/wireless/bcm4329  
RUN cp -r ../bcmon/bcm4329/driver/src/bcm4329 drivers/net/wireless/bcm4329  
  
ENV M /root/kernel/drivers/net/wireless/bcm4329  
  
RUN wget "https://bugzilla.kernel.org/attachment.cgi?id=33502" -O patch8.diff
&& \  
patch -p1 < patch8.diff && \  
rm patch8.diff  
  
RUN wget
http://download.cyanogenmod.org/get/jenkins/2832/cm-7.2.0-fascinatemtd.zip &&
\  
unzip cm-7.2.0-fascinatemtd.zip boot.img && \  
tail -c +8002 boot.img | unlzma > zImage && \  
../extract-symvers.py -B 0xc0008000 zImage > Module.symvers && \  
scripts/extract-ikconfig boot.img > .config && \  
rm zImage boot.img cm-7.2.0-fascinatemtd.zip  
  
CMD make modules && sed -i 's/g9f2f56b/g07dc0db/'
drivers/net/wireless/bcm4329/bcm4329.ko  

