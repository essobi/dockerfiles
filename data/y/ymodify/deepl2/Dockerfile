# Required Environment Variables:  
# $DEEPL2_DISCORD_CHANNEL  
# $DEEPL2_DISCORD_TOKEN  
# $DEEPL2_S3_BUCKET_NAME  
# $DEEPL2_BRANCH_NAME  
# $DEEPL2_COMMIT_ID  
# $AWS_ACCESS_KEY_ID  
# $AWS_SECRET_ACCESS_KEY  
  
FROM debian:stretch-slim  
  
ENV DEEPL2_YAMAX_VERSION=4.0  
  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
  
RUN buildDeps='libopenmpi-dev python3-wheel python3-dev libffi-dev python3-pip
libssl-dev build-essential'; \  
set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests -qq git
openmpi-bin ssh ffmpeg python3 python3-tk $buildDeps \  
&& pip3 install pipenv \  
&& pip3 install awscli \  
&& git clone https://github.com/Y-modify/deepl2 /deepl2 --depth 1 \  
&& cd /deepl2 \  
&& git clone https://github.com/openai/baselines --depth 1 \  
&& sed -i -e 's/mujoco,atari,classic_control,robotics/classic_control/g'
baselines/setup.py \  
&& pip3 install baselines/ \  
&& pipenv install --skip-lock --system \  
&& rm baselines -r \  
&& pip3 uninstall pipenv --yes \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /root/.cache  
  
WORKDIR /deepl2  
  
ADD
https://github.com/Y-modify/YamaX/releases/download/${DEEPL2_YAMAX_VERSION}/YamaX_${DEEPL2_YAMAX_VERSION}.urdf
/deepl2/yamax.urdf  
  
COPY run.sh /deepl2/run.sh  
  
CMD ["./run.sh"]  

