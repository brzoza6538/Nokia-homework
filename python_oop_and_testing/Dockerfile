FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl wget tar xz-utils ca-certificates bzip2 \
    libgtk-3-0 libdbus-glib-1-2 libxt6 libx11-xcb1 libdrm2 libxcomposite1 libxdamage1 libxrandr2 \
    libasound2 libcups2 libatk1.0-0 libatk-bridge2.0-0 libpci3 libxfixes3 libxrender1 libxss1 libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/firefox.tar.xz "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && \
    tar -xJf /tmp/firefox.tar.xz -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox

RUN pip install get-gecko-driver && \
    get-gecko-driver --download-latest --extract && \
    ln -s /app/geckodriver/*/bin/geckodriver /usr/bin/geckodriver

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY robot_tests/ robot_tests/
COPY tests/ tests/
COPY src/ src/

ENV PYTHONPATH=/app
CMD ["robot", "--outputdir", "/app/output", "-P", "src", "robot_tests/robot_test.robot"]
