FROM ubuntu

RUN apt-get update -y
RUN apt-get install --yes build-essential libc6 gfortran g++ wget
WORKDIR /home
RUN wget https://store.enthought.com/downloads/canopy/rh5/64/free/ \
    -O canopy.sh -nv
RUN chmod +x canopy.sh
RUN ./canopy.sh -b
RUN /root/Canopy/canopy_cli --no-gui-setup --install-dir /usr/local
RUN echo "export PATH=/usr/local/Canopy_64bit/System/bin:$PATH" >> /root/.bashrc
RUN echo "EPD_auth = 'aG9ydGFAZWJpLmFjLnVrOkVpbnN0ZWluZnR3MTIzIQ=='" \
    >> /root/.enstaller4rc
RUN /usr/local/Canopy_64bit/System/bin/enpkg --update-all --yes
RUN /usr/local/Canopy_64bit/System/bin/enpkg cython --no-autoupdate \
    --forceall --yes
RUN /usr/local/Canopy_64bit/System/bin/enpkg scipy h5py matplotlib pandas \
    --no-autoupdate --forceall --yes
