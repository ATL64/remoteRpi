FROM	resin/rpi-raspbian:stretch

RUN	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys \
		CC28DD82EF4C718C \
	&& echo "deb http://apt.pilight.org/ stable main" > /etc/apt/sources.list.d/pilight.list \
	&& apt-get update \
	&& apt-get install -y \
		pilight=8.0.2 \
		pilight-webgui=8.0 \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

CMD 	["/usr/local/sbin/pilight-daemon", "-F"]
