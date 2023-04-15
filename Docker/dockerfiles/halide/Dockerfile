#基本的な情報
FROM ubuntu:18.04
MAINTAINER h-kimura
ARG USER=builder
ARG UID
ARG GID
ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive

#必要なパッケージのダウンロード
RUN sed -i'' 's/archive.ubuntu.com/jp.archive.ubuntu.com/' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y
RUN apt-get purge avahi-daemon 
RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y install sudo x11-apps emacs openssh-server iputils-ping net-tools
RUN apt-get -y install git g++ build-essential
RUN apt-get -y install cmake curl zip unzip tar
RUN apt-get -y install software-properties-common
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN add-apt-repository "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-12 main"
RUN apt update
RUN apt-get -y install llvm-12 lldb-12 llvm-12-dev llvm-12-runtime clang-12
RUN apt-get -y install libz-dev pybind11-dev python3-pip libpng-dev libjpeg-dev libcurl4-openssl-dev python python-pip
RUN pip install GitPython

ARG NDK_VERSION="android-ndk-r23b"
ARG NDK_SHA="f47ec4c4badd11e9f593a8450180884a927c330d"
RUN curl --silent --show-error --location --fail --retry 3 \
    --output /tmp/$NDK_VERSION.zip \
    https://dl.google.com/android/repository/$NDK_VERSION-linux.zip
RUN echo "$NDK_SHA /tmp/$NDK_VERSION.zip" > /tmp/$NDK_VERSION.zip.sha1
RUN sha1sum -c /tmp/$NDK_VERSION.zip.sha1
ARG ANDROID_SDK_ROOT="/home/android_sdk"
RUN mkdir $ANDROID_SDK_ROOT \
    && rm -rf $ANDROID_SDK_ROOT/ndk-bundle \
    && unzip -q /tmp/$NDK_VERSION.zip -d $ANDROID_SDK_ROOT \
    && mv $ANDROID_SDK_ROOT/$NDK_VERSION $ANDROID_SDK_ROOT/ndk-bundle \
    && chown -R root:root $ANDROID_SDK_ROOT/ndk-bundle \
    && rm -f /tmp/$NDK_VERSION*

# パスワードやユーザ名の設定
RUN groupadd -g ${GID} ${USER} | true
RUN useradd -u ${UID} -m ${USER} -g ${GID}
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:test" | chpasswd
USER ${USER}
ENV HOME /home/${USER}
WORKDIR ${HOME}
ENV LLVM_CONFIG=llvm-config-12

#halideのダウンロード
RUN git clone https://github.com/halide/Halide.git && cd Halide && git checkout d48fbde357d6e84c04ec69eb32fece2e8584f77b && make -j4 && make test_tutorial -j4
ENV PATH $PATH:$ANDROID_SDK_ROOT/ndk-bundle
